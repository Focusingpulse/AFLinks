# Rex Archive Indexer v2 - Streaming JSON output
# Builds a structured JSON database from all markdown and PDF files in docs/

$ErrorActionPreference = "SilentlyContinue"
$docsPath = "D:\rex_archive\docs"
$outputPath = "D:\rex_archive\index.json"

# Aetherforce WordPress categories (from their site taxonomy)
$categoryKeywords = @{
    "Aether Physics" = @("aether","ether","vacuum energy","zero point","zpe","orgone","prana","chi","vital force","formative force","tachyon","scalar","radiant energy","cosmic energy","vril","od","odic","telluric","eloptic","implosion","vortex","counterspace","hadronic","reciprocal system","schappeller","keely","svp","sympathetic vibratory")
    "Agriculture" = @("agriculture","biodynamic","cosmological botany","electroculture","ancient agriculture","permaculture","compost","farming","crop","fertilizer","mulch","humus")
    "Architecture" = @("architecture","building","goethean architecture","steiner architecture","subtle-energy building")
    "Biology" = @("biology","bioholography","biomimicry","biophoton","creation of life","electrobiology","etheric critters","genetics","goethean morphology","heart science","holographic genetics","merkl","morphogenetics","morphogenesis","morphology","royal rife","rife","regeneration","spontaneous evolution","transmutation","terrain theory")
    "Borderland Research" = @("borderland","alison davidson","gerry vassilatos","vassilatos","jorge resines","michael theroux","thomas joseph brown","trevor james constable","trevor constable")
    "Chemistry" = @("chemistry","alchemy","transmutation","cosmological chemistry","fuel cell","fusion","kolisko","material science","periodic table")
    "Consciousness" = @("consciousness","anthroposophy","esoterica","yoga","kundalini","meditation","spiritual","mind")
    "Crystals" = @("crystal","crystallography","quasicrystal","vogel","kolisko")
    "Electric Universe" = @("electric universe","plasma","dielectric","electrostatic","earth battery","electret","electrical engineering","ground radio","birkeland","alfven","peratt","thornhill","talbott","stars","stellar","nebula")
    "Fallacies of Standard Model" = @("standard model","big bang","relativity","quantum mechanics","atomism","mainstream science","dogma","paradigm","fallacy","fallacies")
    "Geometry" = @("geometry","sacred geometry","cymatics","fractal","golden ratio","phi","fibonacci","harmonics","numbers","projective geometry","platonic","symmetry","toroid")
    "Goethean Science" = @("goethe","goethean","phenomenology","holistic science","morphology","epistemology","qualitative","observation","delicate empiricism","metamorphosis","botany")
    "Gravity" = @("gravity","antigravity","levitation","ufo","counterbary","dean drive","electrogravitics","biefeld-brown")
    "Language" = @("language","trivium","grammar","rhetoric","logic")
    "Life Force" = @("life force","aura","biofield","eloptic","ethers","odic","orgone","telluric","torsion","vril","prana","chi","qi")
    "Light" = @("light","color","colour","optics","spectrum","prism","luminescence","fluorescence","phosphorescence","photoluminescence","spectrochrome","dinshah","light therapy","microscopy","superluminal","astronomy","infrared","ultraviolet","led","laser")
    "Magnetism" = @("magnetism","magnetic","coral castle","diamagnetism","glowing magnetism","paramagnetism","magnet","electromagnet")
    "Natural Philosophy" = @("natural philosophy","philosophy","nature","wholeness","unity","multiplicity")
    "Psychotronics" = @("psychotronics","radionics","radiesthesia","dowsing","pendulum","biogeometry","earth grid","eidetic","psionics","remote viewing","shape power","siddhis","esp","weather engineering","subtle energy","bioresonance","frequency therapy","homeopathy","potentization")
    "Renewable Energy" = @("renewable energy","compressed air","solar","wind","hydro","geothermal","fuel additive","hydrogen","electrolysis")
    "Suppression" = @("suppression","suppressed","censored","banned","hidden","cover-up","conspiracy")
    "Time" = @("time","chronology","chronocraft","time travel","temporal","kozyrev","torsion")
    "Water" = @("water","structured water","memory","pollack","ez water","exclusion zone","nanobubble","cavitation","sonoluminescence","flowforms","schauberger","homeopathy","dew","condensation","hydration","colloid","solution")
    "Material Sciences" = @("material","nanoparticle","graphene","siloxene","crystal","mineral","metallurgy","alloy","ceramic","polymer","plastic","nanotechnology","nanopool","spray-on glass","supramolecular")
    "Transhumanism" = @("transhuman","implant","cyborg","neural","brain computer","bci","genetic engineering","gmo","nanobot","surveillance","rfid","chip","singularity","geo-engineering")
    "Energy Generation" = @("generator","over-unity","free energy","motor","engine","fuel cell","combustion","power wheel","testatika","methernitha","papp","noble gas","electrostatic generator")
    "Health Medicine" = @("cancer","therapy","treatment","healing","medical","disease","virus","bacteria","immune","blood","cell","tissue","dental","tooth","gingivitis","glyoxylide","koch","electrotherapy","radiation therapy")
    "Transportation" = @("airplane","car","vehicle","boat","ship","propulsion","drive","wheel","wing","aircraft","freon","compressed air car","paraplane","vacuplane")
    "Environmental" = @("water treatment","sewage","pollution","remediation","nuclear","radiation","waste","filter","purification","desalination","fog collector","air well")
    "Construction" = @("building","concrete","cement","insulation","heating","cooling","ventilation","structure","candle heater","ice dam")
}

# Patent number regex patterns
$patentRegex = [regex]"(US\s*\d{1,3}[,\.]?\d{3}[,\.]?\d{3}|WO\s*\d{4}/\d{6}|EP\s*\d{7}|CN\s*\d{7,}|JP\s*\d{7,}|KR\s*\d{7,}|DE\s*\d{6,}|GB\s*\d{6,}|FR\s*\d{6,})"

Write-Host "Starting index build v2 at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')..."

$files = Get-ChildItem -Path $docsPath -File
$totalFiles = $files.Count
Write-Host "Found $totalFiles files to index"

# Stream JSON to file
$writer = [System.IO.StreamWriter]::new($outputPath, $false, [System.Text.Encoding]::UTF8)
$writer.Write("[")

$counter = 0
$first = $true

foreach ($file in $files) {
    $counter++
    
    if ($counter % 1000 -eq 0) {
        Write-Host "Processed $counter / $totalFiles files..."
    }
    
    $filename = $file.Name
    $ext = $file.Extension
    $title = [System.IO.Path]::GetFileNameWithoutExtension($filename)
    $sourceUrl = ""
    $categories = @()
    $patents = @()
    $primaryPerson = ""
    
    if ($ext -eq ".md") {
        # Read first 30 lines only for speed
        $lines = Get-Content -Path $file.FullName -TotalCount 30 -ErrorAction SilentlyContinue
        $headerText = ($lines -join " ")
        
        # Extract title from first H1
        foreach ($line in $lines) {
            if ($line -match "^#\s+(.+)$") {
                $title = $matches[1].Trim()
                break
            }
        }
        
        # Extract source URL
        if ($headerText -match "Source:\s*(https?://\S+)") {
            $sourceUrl = $matches[1]
        }
        
        # Build search text from filename + title + first 30 lines
        $searchText = ($title + " " + $filename + " " + $headerText).ToLower()
        
        # Categorize
        foreach ($catName in $categoryKeywords.Keys) {
            foreach ($keyword in $categoryKeywords[$catName]) {
                if ($searchText -match [regex]::Escape($keyword)) {
                    $categories += $catName
                    break
                }
            }
        }
        
        # Extract patent numbers
        $patMatches = $patentRegex.Matches($searchText)
        if ($patMatches.Count -gt 0) {
            $patents = @($patMatches | ForEach-Object { $_.Value -replace '\s+', ' ' } | Select-Object -Unique)
        }
        
        # Extract primary person from title (pattern: "FirstName LASTNAME --" or "FirstName LASTNAME patent")
        if ($title -match "^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+[A-Z][A-Za-z]+)") {
            $primaryPerson = $matches[1]
        }
    }
    
    # Build JSON entry manually (fast)
    $catsJson = '["' + ($categories -join '","') + '"]'
    $patsJson = '["' + ($patents -join '","') + '"]'
    
    # Escape strings for JSON
    $titleEsc = $title -replace '\\', '\\' -replace '"', '\"'
    $urlEsc = $sourceUrl -replace '\\', '\\' -replace '"', '\"'
    $personEsc = $primaryPerson -replace '\\', '\\' -replace '"', '\"'
    $fnameEsc = $filename -replace '\\', '\\' -replace '"', '\"'
    
    if (-not $first) { $writer.Write(",") }
    $first = $false
    
    $jsonEntry = '{"id":' + $counter + ',"filename":"' + $fnameEsc + '","title":"' + $titleEsc + '","extension":"' + $ext + '","size_bytes":' + $file.Length + ',"source_url":"' + $urlEsc + '","categories":' + $catsJson + ',"patent_numbers":' + $patsJson + ',"primary_person":"' + $personEsc + '","last_modified":"' + $file.LastWriteTime.ToString("yyyy-MM-dd") + '"}'
    $writer.Write($jsonEntry)
}

$writer.Write("]")
$writer.Close()

Write-Host "Done! Index written to $outputPath"
Write-Host "Total entries: $counter"

# Print category distribution
Write-Host "`nCategory Distribution:"
$json = Get-Content $outputPath -Raw
$index = $json | ConvertFrom-Json
$catStats = @{}
foreach ($entry in $index) {
    foreach ($cat in $entry.categories) {
        if ($catStats.ContainsKey($cat)) { $catStats[$cat]++ }
        else { $catStats[$cat] = 1 }
    }
}
$catStats.GetEnumerator() | Sort-Object Value -Descending | ForEach-Object {
    Write-Host "  $($_.Key): $($_.Value)"
}

$uncat = ($index | Where-Object { $_.categories.Count -eq 0 -and $_.extension -eq ".md" }).Count
Write-Host "`nUncategorized .md files: $uncat"
$withPatents = ($index | Where-Object { $_.patent_numbers.Count -gt 0 }).Count
Write-Host "Files with patent numbers: $withPatents"
$withPerson = ($index | Where-Object { $_.primary_person -ne "" }).Count
Write-Host "Files with identified person: $withPerson"

Write-Host "`nFinished at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
