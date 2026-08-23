# Rex Archive Indexer v3 - Fixed bugs + better categorization
$ErrorActionPreference = "SilentlyContinue"
$docsPath = "D:\rex_archive\docs"
$outputPath = "D:\rex_archive\index.json"

$categoryKeywords = @{
    "Aether Physics" = @("aether","ether","vacuum energy","zero point","zpe","orgone","prana","chi","vital force","formative force","tachyon","scalar","radiant energy","cosmic energy","vril","od","odic","telluric","eloptic","implosion","vortex","counterspace","hadronic","reciprocal system","schappeller","keely","svp","sympathetic vibratory","scalar potential","whittaker","hodowanec","rhysmonic","testatika","methernitha","baumann","koldomasov","guillemette","perpetual electrostatic","over-unity","over unity","free energy","zero-point")
    "Agriculture" = @("agriculture","biodynamic","cosmological botany","electroculture","ancient agriculture","permaculture","compost","farming","crop","fertilizer","mulch","humus","soil","paramagnetism","callahan","terrastar","ward keith","hemp husbandry","duckweed","ethanol","biomass")
    "Architecture" = @("architecture","goethean architecture","steiner architecture","subtle-energy building")
    "Biology" = @("biology","bioholography","biomimicry","biophoton","creation of life","electrobiology","etheric critters","genetics","goethean morphology","heart science","holographic genetics","merkl","morphogenetics","morphogenesis","morphology","royal rife","rife","regeneration","spontaneous evolution","transmutation","terrain theory","biological transmutation","kurashov","sahno","thiobacillus","crocodylus","peptide","aids","fuchs","beta-catenin","alopecia","bone scaffold","lyngstadaas","dunae","dunaevskij","kolisko","abiogenesis","morley martin","montagnier","dna wave","biocomputer")
    "Borderland Research" = @("borderland","alison davidson","gerry vassilatos","vassilatos","jorge resines","michael theroux","theroux","thomas joseph brown","trevor james constable","trevor constable","borderland science","research foundation")
    "Chemistry" = @("chemistry","alchemy","transmutation","cosmological chemistry","fuel cell","fusion","kolisko","material science","periodic table","siloxene","silox","kautsky","nanoporous","photoluminescent","nanoflowers","molybdenum","disulfide","supramolecular","plastic","nanopool","spray-on glass","graphene","nair")
    "Consciousness" = @("consciousness","anthroposophy","esoterica","yoga","kundalini","meditation","spiritual","mind","hypnosis","kahne","multiple mentality","pleiades","semajase","plejara","prophecy","nelson","american prophecy","age of reason")
    "Crystals" = @("crystal","crystallography","quasicrystal","vogel","kolisko")
    "Electric Universe" = @("electric universe","plasma","dielectric","electrostatic","earth battery","electret","electrical engineering","ground radio","birkeland","alfven","peratt","thornhill","talbott","stars","stellar","nebula","townsend brown","tt brown","electrogravitic","electrogravitics","biefeld","brown","amplituhedron","arkani-hamed","trnka")
    "Fallacies of Standard Model" = @("standard model","big bang","relativity","quantum mechanics","atomism","mainstream science","dogma","paradigm","fallacy","fallacies","second law","thermodynamics")
    "Geometry" = @("geometry","sacred geometry","cymatics","fractal","golden ratio","phi","fibonacci","harmonics","numbers","projective geometry","platonic","symmetry","toroid","fresnel","spiral reflector","steenblik")
    "Goethean Science" = @("goethe","goethean","phenomenology","holistic science","epistemology","qualitative","delicate empiricism","metamorphosis","botany","holdrege","talbott","morrisson","sorce theory","spinbitz","wolfgang peter","formative powers")
    "Gravity" = @("gravity","antigravity","anti-gravity","levitation","ufo","counterbary","dean drive","electrogravitics","biefeld-brown","george arlinski","chronocraft","wilbert smith","project magnet","lanier","paraplane","vacuplane","space drive","norman dean")
    "Language" = @("language","trivium","grammar","rhetoric","logic")
    "Life Force" = @("life force","aura","biofield","eloptic","ethers","odic","orgone","telluric","torsion","vril","prana","chi","qi","reich","core","cosmic orgone","heliognosis","life energy","bioenergy","biogeometry")
    "Light" = @("light","color","colour","optics","spectrum","prism","luminescence","fluorescence","phosphorescence","photoluminescence","spectrochrome","dinshah","light therapy","microscopy","superluminal","astronomy","infrared","ultraviolet","led","laser","babbit","edwin babbit","rudolf steiner","colour theory")
    "Magnetism" = @("magnetism","magnetic","coral castle","diamagnetism","glowing magnetism","paramagnetism","magnet","electromagnet","iron nitride","wang","johannessson","air lubrication","magnetic cellulose","olsson","barbat","self-sustaining","guillemette")
    "Natural Philosophy" = @("natural philosophy","philosophy","wholeness","unity","multiplicity","form of wholeness","age of reason","citizen advertiser")
    "Psychotronics" = @("psychotronics","radionics","radiesthesia","dowsing","pendulum","biogeometry","earth grid","eidetic","psionics","remote viewing","shape power","siddhis","esp","weather engineering","subtle energy","bioresonance","frequency therapy","homeopathy","potentization","ighina","pier luigi","priore","antonine priore","rubtsov","puke ray","led incapacitator")
    "Renewable Energy" = @("renewable energy","compressed air","solar","wind","hydro","geothermal","fuel additive","hydrogen","electrolysis","meyer","stanley meyer","papp","noble gas","guy negre","freon","minto","power wheel","candle heater","air well","frank theilow","dew harvesting","fog collector","chhatre","wave power","farley","rainey","anaconda","roger hine","derek hine","thermal equalizer","avedon","heat from air","huston","kasmer","hydristor","gadgetman","hatton","groove","bartholomew","carbon monoxide","bauer","ecklin","darragh","vi-aqua","rf water","electrolyzed","saline","chlorozone","gwynn","davalos","rubinsky","electric pulses","cancer","glyoxylide","koch","nara","gingivitis","dental","toothpaste","hydroxapatite","yamagishi","orthodontic","belfor","peptide","aids","prion","deactivation","dca","pharm","tox","dmso","medicine")
    "Suppression" = @("suppression","suppressed","censored","banned","hidden","cover-up","conspiracy","covid","narrative","database")
    "Time" = @("time","chronology","chronocraft","time travel","temporal","kozyrev","torsion")
    "Water" = @("water","structured water","memory","pollack","ez water","exclusion zone","nanobubble","cavitation","sonoluminescence","flowforms","schauberger","homeopathy","dew","condensation","hydration","colloid","solution","graphene water","nair","nanobubble generator","sewage","pooloo","kraig johnson","desalination","electrosmosis","oil","wave pump","bellocq","toribio","intermittent absorption","refrigeration","phonon","resonance","energy-storage membrane","xie xian ning","crossbow","science mechanics","whatsanevo","evo")
    "Material Sciences" = @("material","nanoparticle","graphene","siloxene","crystal","mineral","metallurgy","alloy","ceramic","polymer","plastic","nanotechnology","nanopool","spray-on glass","supramolecular","iron nitride","wang","molybdenum","disulfide","nanoflowers","photoluminescent","nanoporous","aluminum oxide","siloxene","kautsky","krishnamoorthy","kurmaev","mondal","nanosheets","supercapacitor")
    "Transhumanism" = @("transhuman","implant","cyborg","neural","brain computer","bci","genetic engineering","gmo","nanobot","surveillance","rfid","chip","singularity","geo-engineering")
    "Energy Generation" = @("generator","over-unity","over unity","free energy","motor","engine","fuel cell","combustion","power wheel","testatika","methernitha","papp","noble gas","electrostatic generator","gunder","graham gunderson","william barbat","self-sustaining","koldomasov","a.i. koldomasov","guillemette","perpetual","electrostatic","hodowanec","rhysmonic","energy extraction","ether","russell","walter russell","coil","tesla","moray king","don smith","smith lagace","kharnoukov","akula","rossi","ecat","lenr","low energy nuclear","andrea rossi","energy catalyzer","steven e. jones","fusion","biberian","berl","protoproduct","bitumen","vegetable waste","kurko","fuel additive","wen-jhy lee","emulsified","water-oil","dunae","dunaevskij","steam engine","samuil","bartholomew","carbon monoxide","engine burns","lambert feher","microwave ignition","internal combustion","bodner","artificial gill","alan-i bodner","negre","compressed air","minto","freon","wallace minto","air well","frank theilow","candle heater","thermal equalizer","avedon","heat from air","huston","kasmer","hydristor","gadgetman","hatton","groove","freon power","johannesson","air lubrication","electrochemical compression","bahar","bamdad bahar","oxygen","hydrogen","electrolysis","meyer","stanley meyer","fuel","darragh","vi-aqua","rf water","austin","david darragh","ozkan","catalyst","production of hydrogen","ethanol","fuel cell")
    "Health Medicine" = @("cancer","therapy","treatment","healing","medical","disease","virus","bacteria","immune","blood","cell","tissue","dental","tooth","gingivitis","glyoxylide","koch","electrotherapy","radiation","davalos","rubinsky","electric pulses","nara","robert nara","hydroxapatite","yamagishi","kazue","orthodontic","belfor","theodore","crocodylus","porusus","peptide","aids","prion","deactivation","dca","pharm","tox","dmso","medicine","fuchs","beta-catenin","alopecia","elaine fuchs","bone scaffold","lyngstadaas","montagnier","dna wave","biocomputer","ross gwynn","chlorozone","electrolyzed","saline","streptococcus","halitosis","tagg","john tagg","cockroach","medicine","karnoukov")
    "Transportation" = @("airplane","car","vehicle","boat","ship","propulsion","drive","wheel","wing","aircraft","freon","compressed air","paraplane","vacuplane","edward lanier","henri melot","steam-oil jet","jet plane","airplane inventions","wing grooves","folding wings","stabilizers","air lubrication","johannesson","bodner","artificial gill","negre","guy negre","wave power","roger hine","derek hine","anaconda","farley","rainey","francis farley","wilks","power wagon","barbat","self-sustaining generator","propulsion","st. clair","john st. clair","bobbin","electromagnetic field","field propulsion")
    "Environmental" = @("water treatment","sewage","pollution","remediation","nuclear","radiation","waste","filter","purification","desalination","fog collector","air well","chhatre","dew harvesting","fukushima","nuclear waste","prion","deactivation","electrosmosis","oil","stephen foley","gold extraction","jiann-tang hwang","microwave steel","fossil fuel","frank pringle","microwave recovery","high-frequency","wave kinetic","attenuating","crossbow","science mechanics","photon","phonon","resonance","energy-storage membrane","xie xian ning","intermittent absorption","refrigeration","ice dam","temporary","candle heater","aetzi","aetzi.mpg","citizen advertiser","dms","whatsanevo","evo","general table","phonon resonance","streptococcus","halitosis","tagg","cockroach","medicine","karnoukov","amranthan","balasingham","agricultural additive","franciszek rychnowski","eteroid","charles russ","eye ray","ray detector","pleiades","semajase","plejara","prophecy","nelson","american prophecy","age of reason","kahne","multiple mentality","hypnosis","catnip","tourmaline","radionics","santilli","magnecule","ruggero","wilhelm reich","orgone","collected articles","john v milewski","ormus","gold from glass","wilbert smith","project magnet","george arlinski","chronocraft","dean drive","norman dean","john campbell","space drive","whittaker","scalar","edmund whittaker","london mathematical","mathematische annalen","scalar potential","amplituhedron","arkani-hamed","trnka","kozyrev","torsion","time","russian cosmism","federov","claude swanson","synchronized universe","sepp hasslberger","peter gariaev","wave genetics","matti pitkanen","topological","geometro","dewey larson","reciprocal systems","glen atkinson","gyroscopic biodynamics","heliognosis","life energy meter","institute for orgonomic","jeffrey volk","cymatic source","john reid","cymascope","standing wave","maryel gardene","atom and octave","richard merrick","interference theory","mark rossi","musica universalis","anthony morris","numerical universe","planetary harmonics","bioresonance","irene caesar","wavegenome","jana dixon","biology of kundalini","hiroshi motoyama","california institute","human science","publications of biofield","thornton streeter","biofield viewer","eileen mccusick","biofield tuning","kilner aura","georges lakhovsky","multiple wave oscillator","robert becker","body electric","dean radin","psi research","barry carter","ormus","jeffrey mishlove","new thinking allowed","master choa kok sui","quantum gravity research","quasicrystals","alien scientist","buckminster fuller","stephen phillips","sacred geometry correspondences","frank chester","chestahedron","decatria","cosmic-core","razon aurea","ananda bosman","vortexijah","dan winter","golden mean implosion","randall carlson","sacred geometry international","intentional species","nick thomas","counterspatial","projective geometry","lawrence edwards","plant life","embassy of free mind","edgeba","alice bailey","blavatsky","treatise on 7 rays","rudolf steiner","anthroposophy","jose arguelles","galactic mayan","law of time","dkmu","chaos magick","mantak chia","universal tao","dr yang jwing ming","vasant lad","ayurvedic","sevan bomar","secret energy","innerversity","bernard guenther","veil of reality","adam mclean","levity","embassy of the mind")
    "Construction" = @("building","concrete","cement","insulation","heating","cooling","ventilation","structure","candle heater","ice dam","crossbow","science mechanics","intermittent absorption","refrigeration","thermal equalizer","avedon","heat from air","huston")
}

# Patent number regex - handles filenames like US2474533A.pdf.md, WO9409894A1.pdf, etc.
$patentRegex = [regex]"((?:US|WO|EP|CN|JP|KR|DE|GB|FR|SU|AT|CA|TW)\s*\d{5,}[A-Z]?\d?)"

# Media file patterns (images, audio, video converted to .md)
$mediaPattern = [regex]"\.(jpg|gif|png|bmp|mp3|mp4|mpg|avi|wav)\.md$"

Write-Host "Starting index build v3 at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')..."

$files = Get-ChildItem -Path $docsPath -File
$totalFiles = $files.Count
Write-Host "Found $totalFiles files to index"

$writer = [System.IO.StreamWriter]::new($outputPath, $false, [System.Text.Encoding]::UTF8)
$writer.Write("[")

$counter = 0
$first = $true
$mediaCount = 0
$patentCount = 0
$personCount = 0

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
    $fileType = "document"
    
    # Check if this is a media file (image/audio/video converted to .md)
    if ($mediaPattern.IsMatch($filename)) {
        $fileType = "media"
        $mediaCount++
    }
    
    if ($ext -eq ".md" -and $fileType -ne "media") {
        # Read first 30 lines only
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
        
        # Build search text
        $searchText = ($title + " " + $filename + " " + $headerText).ToLower()
        
        # Categorize
        foreach ($catName in $categoryKeywords.Keys) {
            foreach ($keyword in $categoryKeywords[$catName]) {
                if ($searchText -match [regex]::Escape($keyword)) {
                    if ($categories -notcontains $catName) {
                        $categories += $catName
                    }
                    break
                }
            }
        }
        
        # Extract patent numbers from filename + content
        $patMatches = $patentRegex.Matches($filename + " " + $headerText)
        if ($patMatches.Count -gt 0) {
            $patents = @()
            foreach ($m in $patMatches) {
                $p = $m.Groups[1].Value -replace '\s+', ' '
                if ($patents -notcontains $p) { $patents += $p }
            }
            if ($patents.Count -gt 0) { $patentCount++ }
        }
        
        # Extract primary person from title
        if ($title -match "^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+[A-Z][A-Za-z]+)") {
            $primaryPerson = $matches[1]
            $personCount++
        }
    } elseif ($fileType -eq "media") {
        # For media files, try to extract patent numbers from filename
        $patMatches = $patentRegex.Matches($filename)
        if ($patMatches.Count -gt 0) {
            $patents = @()
            foreach ($m in $patMatches) {
                $p = $m.Groups[1].Value -replace '\s+', ' '
                if ($patents -notcontains $p) { $patents += $p }
            }
        }
    }
    
    # Build JSON entry
    if ($categories.Count -eq 0) {
        $catsJson = "[]"
    } else {
        $catsJson = '["' + ($categories -join '","') + '"]'
    }
    
    if ($patents.Count -eq 0) {
        $patsJson = "[]"
    } else {
        $patsJson = '["' + ($patents -join '","') + '"]'
    }
    
    $titleEsc = $title -replace '\\', '\\' -replace '"', '\"'
    $urlEsc = $sourceUrl -replace '\\', '\\' -replace '"', '\"'
    $personEsc = $primaryPerson -replace '\\', '\\' -replace '"', '\"'
    $fnameEsc = $filename -replace '\\', '\\' -replace '"', '\"'
    
    if (-not $first) { $writer.Write(",") }
    $first = $false
    
    $jsonEntry = '{"id":' + $counter + ',"filename":"' + $fnameEsc + '","title":"' + $titleEsc + '","type":"' + $fileType + '","extension":"' + $ext + '","size_bytes":' + $file.Length + ',"source_url":"' + $urlEsc + '","categories":' + $catsJson + ',"patent_numbers":' + $patsJson + ',"primary_person":"' + $personEsc + '","last_modified":"' + $file.LastWriteTime.ToString("yyyy-MM-dd") + '"}'
    $writer.Write($jsonEntry)
}

$writer.Write("]")
$writer.Close()

Write-Host "Done! Index written to $outputPath"
Write-Host "Total entries: $counter"
Write-Host "Media files: $mediaCount"
Write-Host "Files with patents: $patentCount"
Write-Host "Files with person: $personCount"

# Print category distribution
Write-Host "`nCategory Distribution:"
$json = Get-Content $outputPath -Raw
$index = $json | ConvertFrom-Json
$catStats = @{}
foreach ($entry in $index) {
    foreach ($cat in $entry.categories) {
        if ($cat -ne "" -and $cat -ne $null) {
            if ($catStats.ContainsKey($cat)) { $catStats[$cat]++ }
            else { $catStats[$cat] = 1 }
        }
    }
}
$catStats.GetEnumerator() | Sort-Object Value -Descending | ForEach-Object {
    Write-Host "  $($_.Key): $($_.Value)"
}

$uncat = ($index | Where-Object { ($_.categories.Count -eq 0) -and $_.type -eq "document" -and $_.extension -eq ".md" }).Count
Write-Host "`nUncategorized document .md files: $uncat"

Write-Host "`nFinished at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
