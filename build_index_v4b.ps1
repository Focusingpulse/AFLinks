# build_index_v4b.ps1 — Rebuild index with URL folder hints + fixed patent regex
$ErrorActionPreference = "SilentlyContinue"
$docsDir = "D:\rex_archive\docs"
$outputFile = "D:\rex_archive\index.json"

$categoryKeywords = @{
    "Aether Physics" = @("aether","ether","zero point","zpe","vacuum energy","casimir","quantum vacuum","scalar wave","longitudinal","radiant energy","cold electricity","subtle energy","tachyon","torsion field","aetheric","etheric","prana","orgone","od ","odic","vril","morphic","morphogenetic","biophotonic","biophoton","formative force","life force","vital force","electrogravitic","monatomic","ormus","orme","overunity","over-unity","fuelless","free energy","zero-point")
    "Energy Generation" = @("free energy","overunity","perpetual","self-running","energy extraction","generator","alternator","power generation","fuelless","magnetic motor","rossi","e-cat","cold fusion","lenr","fusion reactor","thermoelectric","tesla coil","energy machine","moray","hendershot","testatika","searl","quantum energy","power device","energy device","newman","bedini","lutec","perendev")
    "Water" = @("water","structured water","ez water","exclusion zone","fourth phase","hexagonal","vortex water","revitalized","nanobubble","desalination","graphene filter","pollack","gel water","interfacial","water memory","water crystal","living water","sacred water","ormus water","alkaline water","ionized","hydration","aqua","water treatment","water purification","electrolysis","schauberger")
    "Magnetism" = @("magnet","magnetic","paramagnetism","diamagnetism","ferromagnetism","electromagnet","neodymium","lodestone","magnetic field","magnetic resonance","magnet motor","magnetism","biomagnetism","magnet therapy","halbach","magnetic levitation","eddy current","permeability","gauss","magnetohydrodynamic","davis","rawls")
    "Gravity" = @("gravity","antigravity","anti-gravity","gravitation","weight reduction","gravitational","g-field","inertia","spacetime","warp drive","gravitomagnetic","graviton","acceleration","centrifugal","centripetal","levitation","buoyancy","podkletnov","tajmar")
    "Light" = @("light","photon","optics","spectrum","color therapy","colour","luminescence","fluorescence","phosphorescence","infrared","ultraviolet","laser","coherent light","biophoton","spectroscopy","refraction","diffraction","polarization","prism","spectrochrome","dinsah","chromotherapy","phototherapy","photonics","fiber optic","dinshah")
    "Electric Universe" = @("plasma","electric universe","birkeland","aurora","solar wind","corona","discharge","ionosphere","magnetosphere","electric sun","plasma cosmology","peratt","alfven","z-pinch","plasma focus","plasma discharge","filament","nebula","cosmology","big bang","cosmic","galaxy","thornhill","talbott","scott")
    "Psychotronics" = @("radionics","radiesthesia","dowsing","pendulum","shape power","psychotronics","psionics","radionic","stick pad","rub plate","witness","reagent","se-5","se5","de la warr","malcolm rae","drown","turenne","isotron","koom","lucas")
    "Consciousness" = @("consciousness","awareness","perception","cognition","psi","esp","remote viewing","telepathy","intuition","sentience","meditation","brainwave","binaural","isochronic","entrainment","neurofeedback","biofeedback","heartmath","coherence","psychedelic","entheogen","ayahuasca","plant medicine","radin","mishlove")
    "Biology" = @("biology","biological","organism","cell ","dna","rna","gene","genetic","embryo","embryology","metamorphosis","evolution","morphic field","epigenetic","membrane","protein","enzyme","bacteria","virus","microbiome","fungi","mycelium","stem cell","regeneration","morphogenesis","tissue","organ","transmutation","kurashov","sahno")
    "Health Medicine" = @("health","medicine","medical","healing","therapy","treatment","disease","cancer","covid","vaccine","immune","nutrition","supplement","herbal","tincture","homeopathy","naturopath","holistic","alternative medicine","detox","antioxidant","longevity","wellness","remedy","clinical","pharmaceutical","frequency healing","rife")
    "Agriculture" = @("agriculture","farming","permaculture","soil","compost","biodynamic","organic farming","crop","plant","garden","seed","mycelium","mushroom","vermicompost","biochar","terra preta","agroecology","regenerative","food forest","polyculture","companion plant","cover crop","mulch","swale","hugelkultur","duckweed","aquaculture")
    "Chemistry" = @("chemistry","chemical","reaction","element","isotope","transmutation","alchemy","spagyric","ormus","orme","monatomic","colloidal","catalyst","oxidation","reduction","molecule","compound","synthesis","electrolysis","acid","alkaline","salt","mineral","biochemical","tetracopper","kanzius")
    "Material Sciences" = @("material","crystal","crystallography","semiconductor","superconductor","nanomaterial","graphene","metamaterial","alloy","metallurgy","ceramic","polymer","composite","nanotube","fullerene","buckminster","buckyball","quantum dot","thin film","lattice","crystalline","quasicrystal")
    "Geometry" = @("geometry","sacred geometry","proportion","golden ratio","phi","fibonacci","fractal","platonic solid","polyhedra","tesselation","pattern","symmetry","vesica","flower of life","metatron","merkaba","spiral","helix","torus","vortex","mathematics","topology","projective","counter-space","chestahedron")
    "Crystals" = @("crystal","quartz","piezoelectric","crystallography","lattice","mineral","gem","amethyst","tourmaline","selenite","shungite","orgonite","crystal skull","crystal grid","crystal healing","gemstone","diamond")
    "Transportation" = @("vehicle","engine","propulsion","thrust","fuel","transportation","aviation","aircraft","ship","diesel","gasoline","electric vehicle","fuel cell","hydrogen","biodiesel","turbo","jet","rocket","spaceship","drone","motor","combustion","steam","stirling")
    "Environmental" = @("environment","pollution","climate","geoengineering","weather","atmosphere","ecosystem","toxin","radiation","emf","electromagnetic pollution","geopathic","earth energy","ley line","geomancy","feng shui","building biology","electromagnetic field","non-native emf","5g","wifi","cell tower","smart meter","chemtrail","haarp")
    "Construction" = @("construction","building","architecture","dome","vaastu","sacred architecture","geodesic","timber","straw bale","cob","hempcrete","earthship","passive house","natural building","green building","sustainable","biotecture","pacific domes")
    "Time" = @("time","temporal","chronology","kozyrev","torsion","time dilation","causality","retrocausal","entropy","arrow of time","cyclic","rhythm","oscillation","frequency","resonance","harmonic","synchronization","swanson","synchronized universe")
    "Life Force" = @("life force","orgone","odic","vril","prana","chi","qi ","subtle energy","biodynamic","biophotonic","etheric","vital force","reich","cloudbuster","orgone accumulator","bion","deadly orgone","dor","cosmic orgone","heliognosis")
    "Suppression" = @("suppression","censorship","conspiracy","cover-up","patent seizure","suppressed invention","fda","epa","classified","secret","black project","military","invention secrecy","gag order","banned","forbidden","lost invention","seizure","order 8550")
    "Goethean Science" = @("goethe","goethean","phenomenology","morphology","metamorphosis","wholeness","holistic science","steiner","anthroposoph","waldorf","biodynamic","etheric","astral","consciousness soul","thinking","cognition","holdrege","talbott")
    "Natural Philosophy" = @("philosophy","epistemology","ontology","nondual","dualism","materialism","reductionism","paradigm","kant","cartesian","post-modern","rational","empirical","qualia","qualitative","holism","systems","complexity","emergence","morrison")
    "Language" = @("language","linguistics","grammar","trivium","rhetoric","dialectic","semantics","semiotics","etymology","phonetics","syntax","logos")
    "Fallacies of Standard Model" = @("standard model","quantum mechanics","relativity","einstein","newton","big bang","dark matter","dark energy","particle physics","quantum field theory","string theory","supersymmetry","higgs","cern","lhc","fallacy","wrong","debunk")
    "Transhumanism" = @("transhumanism","transhuman","geoengineering","chemtrail","weather modification","haarp","5g","surveillance","mind control","biometric","microchip","artificial intelligence","technocracy","digital id","cbdc","social credit","internet of things","nanotech","nanoparticle","mrna","gene editing","crispr","gain of function","covid","vaccine")
    "Borderland Research" = @("borderland","frontier science","alternative science","suppressed science","unexplained","anomalous","fortean","charles fort","anomaly","paranormal","parapsychology","unconventional","fringe","edge science")
    "Renewable Energy" = @("solar","wind","hydro","geothermal","biomass","renewable","sustainable","clean energy","photovoltaic","battery","fuel cell","hydrogen","biofuel","algae","stirling","tidal","wave energy","thermoelectric")
}

# Rex Research folder name -> category hints (deduplicated)
$folderCategoryHints = @{
    "meyerhy" = @("Energy Generation","Water")
    "tetracopper" = @("Chemistry","Material Sciences")
    "biophotons" = @("Biology","Light","Consciousness")
    "xtlradio" = @("Aether Physics","Light")
    "sahnokurashov" = @("Biology","Chemistry")
    "nairgraphene" = @("Water","Material Sciences")
    "hurtubis" = @("Aether Physics","Borderland Research")
    "HodowanecRhysmonics" = @("Aether Physics","Energy Generation")
    "stuff" = @("Borderland Research")
    "covidatabase" = @("Health Medicine","Transhumanism")
    "fuchs" = @("Biology","Health Medicine")
    "nanobubblegener" = @("Water")
    "usa" = @("Borderland Research","Suppression")
    "ketchum" = @("Energy Generation","Transportation")
    "aether" = @("Aether Physics")
    "energy" = @("Energy Generation")
    "water" = @("Water")
    "magnet" = @("Magnetism")
    "gravity" = @("Gravity")
    "tesla" = @("Aether Physics","Energy Generation")
    "orgone" = @("Life Force")
    "reich" = @("Life Force")
    "schauberger" = @("Water","Energy Generation")
    "pollack" = @("Water")
    "plasma" = @("Electric Universe")
    "radionics" = @("Psychotronics")
    "radiesthesia" = @("Psychotronics")
    "goethe" = @("Goethean Science")
    "steiner" = @("Goethean Science")
    "crystal" = @("Crystals","Material Sciences")
    "light" = @("Light")
    "color" = @("Light")
    "colour" = @("Light")
    "health" = @("Health Medicine")
    "medicine" = @("Health Medicine")
    "cancer" = @("Health Medicine")
    "covid" = @("Health Medicine","Transhumanism")
    "agriculture" = @("Agriculture")
    "farm" = @("Agriculture")
    "permaculture" = @("Agriculture")
    "chemistry" = @("Chemistry")
    "alchemy" = @("Chemistry")
    "ormus" = @("Chemistry","Life Force")
    "material" = @("Material Sciences")
    "graphene" = @("Material Sciences","Water")
    "nanotube" = @("Material Sciences")
    "geometry" = @("Geometry")
    "sacred" = @("Geometry")
    "transport" = @("Transportation")
    "engine" = @("Transportation","Energy Generation")
    "motor" = @("Transportation","Energy Generation")
    "fuel" = @("Transportation","Energy Generation")
    "environment" = @("Environmental")
    "geoeng" = @("Environmental","Transhumanism")
    "weather" = @("Environmental")
    "climate" = @("Environmental")
    "construction" = @("Construction")
    "architecture" = @("Construction")
    "dome" = @("Construction")
    "time" = @("Time")
    "kozyrev" = @("Time")
    "torsion" = @("Time","Aether Physics")
    "scalar" = @("Aether Physics")
    "longitudinal" = @("Aether Physics")
    "consciousness" = @("Consciousness")
    "mind" = @("Consciousness")
    "psi" = @("Consciousness")
    "biology" = @("Biology")
    "dna" = @("Biology")
    "embryo" = @("Biology")
    "transmutation" = @("Chemistry","Biology")
    "suppression" = @("Suppression")
    "fort" = @("Borderland Research")
    "borderland" = @("Borderland Research")
    "freeenergy" = @("Energy Generation")
    "free energy" = @("Energy Generation")
    "overunity" = @("Energy Generation")
    "zero" = @("Aether Physics")
    "vacuum" = @("Aether Physics")
    "fusion" = @("Energy Generation")
    "hydrogen" = @("Energy Generation","Water")
    "solar" = @("Renewable Energy","Light")
    "wind" = @("Renewable Energy")
    "battery" = @("Renewable Energy")
    "geothermal" = @("Renewable Energy")
    "transhuman" = @("Transhumanism")
    "haarp" = @("Transhumanism","Environmental")
    "5g" = @("Transhumanism","Environmental")
    "chemtrail" = @("Transhumanism","Environmental")
    "vaccine" = @("Health Medicine","Transhumanism")
    "rife" = @("Health Medicine")
    "frequency" = @("Health Medicine","Consciousness")
    "healing" = @("Health Medicine")
    "emf" = @("Environmental")
    "geopathic" = @("Environmental")
    "ley" = @("Environmental")
    "dowsing" = @("Psychotronics","Environmental")
    "biogeometry" = @("Psychotronics","Environmental")
    "vaastu" = @("Construction","Geometry")
    "vastu" = @("Construction","Geometry")
    "fengshui" = @("Environmental","Construction")
    "cymatics" = @("Geometry","Consciousness")
    "harmonics" = @("Geometry","Time")
    "sound" = @("Consciousness","Geometry")
    "vibration" = @("Consciousness")
    "resonance" = @("Aether Physics","Consciousness")
    "ether" = @("Aether Physics")
    "neurofeedback" = @("Consciousness")
    "brainwave" = @("Consciousness")
    "meditation" = @("Consciousness")
    "remote" = @("Consciousness")
    "telepathy" = @("Consciousness")
    "antigravity" = @("Gravity")
    "anti-gravity" = @("Gravity")
    "levitation" = @("Gravity")
    "propulsion" = @("Transportation","Gravity")
    "ufo" = @("Transportation","Borderland Research")
    "uap" = @("Transportation","Borderland Research")
    "coldfusion" = @("Energy Generation","Chemistry")
    "lenr" = @("Energy Generation","Chemistry")
    "meyer" = @("Energy Generation","Water")
    "moray" = @("Energy Generation")
    "hendershot" = @("Energy Generation")
    "searl" = @("Energy Generation","Magnetism")
    "newman" = @("Energy Generation")
    "bedini" = @("Energy Generation")
    "rossi" = @("Energy Generation","Chemistry")
    "papp" = @("Energy Generation")
    "perendev" = @("Energy Generation","Magnetism")
    "godin" = @("Gravity")
    "roschin" = @("Gravity")
    "podkletnov" = @("Gravity")
    "tajmar" = @("Gravity")
    "brown" = @("Gravity","Aether Physics")
    "biefeld" = @("Gravity","Aether Physics")
    "lifter" = @("Gravity","Aether Physics")
    "ion" = @("Aether Physics","Gravity")
    "electrogravitic" = @("Gravity","Aether Physics")
    "sperry" = @("Aether Physics")
    "royalrife" = @("Health Medicine")
    "nesara" = @("Suppression")
    "secrecy" = @("Suppression")
    "patent" = @("Suppression")
    "invention" = @("Energy Generation")
    "perpetual" = @("Energy Generation")
    "over" = @("Energy Generation")
    "selfrunning" = @("Energy Generation")
    "fuelless" = @("Energy Generation")
    "kinetic" = @("Energy Generation")
    "thermodynamic" = @("Energy Generation")
    "entropy" = @("Time","Aether Physics")
    "quantum" = @("Aether Physics")
    "wave" = @("Aether Physics","Light")
    "field" = @("Aether Physics")
    "electric" = @("Aether Physics")
    "magnetic" = @("Magnetism")
    "gravit" = @("Gravity")
    "photon" = @("Light")
    "optic" = @("Light")
    "spectro" = @("Light")
    "therapy" = @("Health Medicine")
    "disease" = @("Health Medicine")
    "nutrition" = @("Health Medicine","Agriculture")
    "herbal" = @("Health Medicine","Agriculture")
    "homeopathy" = @("Health Medicine")
    "detox" = @("Health Medicine")
    "immune" = @("Health Medicine")
    "soil" = @("Agriculture")
    "compost" = @("Agriculture")
    "seed" = @("Agriculture")
    "plant" = @("Agriculture","Biology")
    "garden" = @("Agriculture")
    "crop" = @("Agriculture")
    "biochar" = @("Agriculture")
    "mushroom" = @("Agriculture","Biology")
    "fungi" = @("Agriculture","Biology")
    "bacteria" = @("Biology")
    "virus" = @("Biology","Health Medicine")
    "cell" = @("Biology")
    "gene" = @("Biology")
    "rna" = @("Biology")
    "evolution" = @("Biology")
    "epigenetic" = @("Biology")
    "stem" = @("Biology")
    "tissue" = @("Biology")
    "organ" = @("Biology","Health Medicine")
    "quartz" = @("Crystals")
    "piezo" = @("Crystals")
    "mineral" = @("Crystals","Material Sciences")
    "gem" = @("Crystals")
    "lattice" = @("Crystals","Material Sciences")
    "semiconductor" = @("Material Sciences")
    "superconductor" = @("Material Sciences")
    "nanomaterial" = @("Material Sciences")
    "fullerene" = @("Material Sciences")
    "alloy" = @("Material Sciences")
    "polymer" = @("Material Sciences")
    "ceramic" = @("Material Sciences")
    "golden" = @("Geometry")
    "fibonacci" = @("Geometry")
    "fractal" = @("Geometry")
    "platonic" = @("Geometry")
    "vesica" = @("Geometry")
    "torus" = @("Geometry","Aether Physics")
    "helix" = @("Geometry","Biology")
    "spiral" = @("Geometry","Aether Physics")
    "vehicle" = @("Transportation")
    "aviation" = @("Transportation")
    "aircraft" = @("Transportation")
    "rocket" = @("Transportation")
    "ship" = @("Transportation")
    "combustion" = @("Transportation")
    "steam" = @("Transportation","Energy Generation")
    "stirling" = @("Energy Generation","Transportation")
    "diesel" = @("Transportation")
    "gasoline" = @("Transportation")
    "pollution" = @("Environmental")
    "atmosphere" = @("Environmental")
    "ecosystem" = @("Environmental")
    "radiation" = @("Environmental","Health Medicine")
    "building" = @("Construction")
    "hempcrete" = @("Construction")
    "cob" = @("Construction")
    "straw" = @("Construction")
    "timber" = @("Construction")
    "causality" = @("Time")
    "cyclic" = @("Time")
    "rhythm" = @("Time")
    "oscillation" = @("Time","Aether Physics")
    "harmonic" = @("Time","Geometry")
    "cloudbuster" = @("Life Force","Environmental")
    "vril" = @("Life Force")
    "chi" = @("Life Force")
    "qi" = @("Life Force")
    "subtle" = @("Life Force","Aether Physics")
    "vital" = @("Life Force")
    "etheric" = @("Life Force","Aether Physics")
    "biophot" = @("Life Force","Light","Biology")
    "anthroposoph" = @("Goethean Science")
    "waldorf" = @("Goethean Science")
    "phenomenology" = @("Goethean Science","Natural Philosophy")
    "morphology" = @("Goethean Science","Biology")
    "philosophy" = @("Natural Philosophy")
    "epistemology" = @("Natural Philosophy")
    "ontology" = @("Natural Philosophy")
    "paradigm" = @("Natural Philosophy")
    "reductionism" = @("Natural Philosophy","Fallacies of Standard Model")
    "materialism" = @("Natural Philosophy","Fallacies of Standard Model")
    "einstein" = @("Fallacies of Standard Model")
    "relativity" = @("Fallacies of Standard Model","Gravity")
    "standardmodel" = @("Fallacies of Standard Model")
    "darkmatter" = @("Fallacies of Standard Model")
    "darkenergy" = @("Fallacies of Standard Model")
    "bigbang" = @("Fallacies of Standard Model","Electric Universe")
    "surveillance" = @("Transhumanism")
    "mindcontrol" = @("Transhumanism","Consciousness")
    "microchip" = @("Transhumanism")
    "nanoparticle" = @("Transhumanism","Material Sciences")
    "mrna" = @("Transhumanism","Health Medicine")
    "crispr" = @("Transhumanism","Biology")
    "anomaly" = @("Borderland Research")
    "paranormal" = @("Borderland Research","Consciousness")
    "unexplained" = @("Borderland Research")
    "fringe" = @("Borderland Research")
    "photovoltaic" = @("Renewable Energy")
    "tidal" = @("Renewable Energy")
    "biomass" = @("Renewable Energy","Agriculture")
    "hydro" = @("Renewable Energy","Water")
    "language" = @("Language")
    "linguistics" = @("Language")
    "grammar" = @("Language")
    "trivium" = @("Language")
}

$metaCategories = @{
    "Aether, Light & Electricity" = @("Aether Physics","Light","Magnetism","Life Force")
    "Plasma, Torsion & Cosmology" = @("Electric Universe","Time","Gravity")
    "Goethean & Anthroposophical Science" = @("Goethean Science","Natural Philosophy","Language")
    "Radionics, Radiesthesia & Shape Power" = @("Psychotronics")
    "Optics & Colour Therapy" = @("Light","Crystals")
    "Biological & Morphogenetic Science" = @("Biology","Health Medicine","Consciousness")
    "Water Structure & Memory" = @("Water","Environmental")
    "Sacred & Projective Geometry" = @("Geometry","Architecture","Construction")
    "Regenerative Agriculture" = @("Agriculture")
    "Material Sciences & Alchemy" = @("Chemistry","Material Sciences")
    "Transhumanism & Psychotronic Warfare" = @("Transhumanism","Suppression")
    "Energy & Transportation" = @("Energy Generation","Renewable Energy","Transportation")
    "Challenges to the Standard Model" = @("Fallacies of Standard Model","Borderland Research")
    "Harmonics, Rhythms & Cycles" = @("Geometry","Time","Crystals")
    "Weather & Geo-Engineering" = @("Environmental","Transhumanism")
}

$binaryExts = @(".pdf",".jpg",".gif",".png",".bmp",".svg",".mp4",".wmv",".avi",".mov",".mp3",".wav",".flac",".ppt",".pptx",".doc",".docx")

Write-Host "Scanning files..."
$allFiles = Get-ChildItem $docsDir -File | Sort-Object Name
$total = $allFiles.Count
Write-Host "Found $total files"

$results = [System.Collections.ArrayList]::new()
$count = 0
$startTime = Get-Date

foreach ($file in $allFiles) {
    $count++
    if ($count % 1000 -eq 0) {
        $elapsed = (Get-Date) - $startTime
        Write-Host "Processing $count / $total... ($([math]::Round($elapsed.TotalSeconds,1))s)"
    }

    $isBinary = $false
    foreach ($ext in $binaryExts) {
        if ($file.Name -like "*$ext" -or $file.Name -like "*$ext.md") { $isBinary = $true; break }
    }

    $entry = [ordered]@{
        id = $count
        filename = $file.Name
        title = $file.BaseName
        type = if ($isBinary) { "media" } else { "document" }
        extension = $file.Extension
        size_bytes = $file.Length
        source_url = ""
        categories = @()
        meta_categories = @()
        patent_numbers = @()
        primary_person = ""
        content_preview = ""
        last_modified = $file.LastWriteTime.ToString("yyyy-MM-dd")
    }

    # Read header for all files; only read more for text files
    $lineCount = if ($isBinary) { 5 } else { 100 }
    $lines = Get-Content $file.FullName -TotalCount $lineCount -ErrorAction SilentlyContinue
    $rawContent = ""
    if ($lines) { $rawContent = $lines -join "`n" }

    # Extract title
    if ($rawContent -match '^#\s+(.+?)[\r\n]') { $entry.title = $matches[1].Trim() }

    # Extract source URL
    if ($rawContent -match 'Source:\s*(https?://[^\s\r\n]+)') { $entry.source_url = $matches[1].Trim() }

    # Get content after --- separator
    $contentBody = $rawContent
    $sepIdx = $rawContent.IndexOf("`n---`n")
    if ($sepIdx -ge 0) { $contentBody = $rawContent.Substring($sepIdx + 5) }

    # Build search text
    $fullSearchText = ($entry.title + " " + $contentBody + " " + $file.Name).ToLower()

    # Extract folder from source URL
    $urlFolder = ""
    if ($entry.source_url -match 'rexresearch\.com/([^/]+)') { $urlFolder = $matches[1].ToLower() }

    # ─── Categorize from content keywords ───
    $matchedCategories = @{}
    foreach ($cat in $categoryKeywords.Keys) {
        foreach ($kw in $categoryKeywords[$cat]) {
            if ($fullSearchText -match [regex]::Escape($kw)) {
                if (-not $matchedCategories.ContainsKey($cat)) { $matchedCategories[$cat] = 0 }
                $matchedCategories[$cat]++
            }
        }
    }

    # ─── Add hints from source URL folder ───
    if ($urlFolder -and $folderCategoryHints.ContainsKey($urlFolder)) {
        foreach ($cat in $folderCategoryHints[$urlFolder]) {
            if (-not $matchedCategories.ContainsKey($cat)) { $matchedCategories[$cat] = 0 }
            $matchedCategories[$cat] += 2
        }
    }
    # Note: partial folder match removed for performance (was O(files*keys))

    $entry.categories = @($matchedCategories.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 5 | ForEach-Object { $_.Key })

    # ─── Meta-categories ───
    $metaCats = @()
    foreach ($meta in $metaCategories.Keys) {
        foreach ($cat in $entry.categories) {
            if ($metaCategories[$meta] -contains $cat -and $metaCats -notcontains $meta) { $metaCats += $meta }
        }
    }
    $entry.meta_categories = $metaCats

    # ─── Patent numbers (case-insensitive) ───
    $patentMatches = [regex]::Matches($fullSearchText, '(?i)\b((?:us|ep|wo|gb|fr|de|jp|kr|cn|ru|su|ca|au|ch|nl|se|it|es|be|at|dk|fi|no|pl|cz|hu|ro|bg|hr|tw|th|mx|br|ar|in|il|nz|za|sg|hk|my|ph|vn|id|pk|eg|sa|ae|tr|ir)(\d{5,}[a-z]?\d*))')
    $patents = @()
    foreach ($m in $patentMatches) {
        $pat = $m.Groups[1].Value.ToUpper()
        if ($patents -notcontains $pat) { $patents += $pat }
    }
    $entry.patent_numbers = @($patents | Select-Object -First 10)

    # ─── Researcher name ───
    if ($entry.title -match '^([A-Z][a-z]+\s+[A-Z][A-Z]+)[\s]*[:\-–]') {
        $entry.primary_person = $matches[1].Trim()
    } elseif ($entry.title -match '^([A-Z][a-z]+\s+[A-Z][a-z]+)\s+--') {
        $entry.primary_person = $matches[1].Trim()
    } elseif ($entry.title -match '^([A-Z][a-z]+\s+[A-Z][A-Z][a-z]+)\s') {
        $entry.primary_person = $matches[1].Trim()
    }

    # ─── Content preview ───
    if (-not $isBinary) {
        $previewText = $contentBody -replace '[^\x20-\x7E]', ' '
        $previewText = $previewText -replace '\s+', ' '
        $previewText = $previewText.Trim()
        if ($previewText.Length -gt 300) { $previewText = $previewText.Substring(0, 300) }
        $entry.content_preview = $previewText
    }

    [void]$results.Add([PSCustomObject]$entry)
}

# ─── Write output ───
Write-Host "Writing index.json..."
$json = $results | ConvertTo-Json -Depth 3 -Compress
[System.IO.File]::WriteAllText($outputFile, $json)

# ─── Stats ───
$elapsed = (Get-Date) - $startTime
Write-Host ""
Write-Host "=== INDEX STATISTICS ==="
Write-Host "Total files: $($results.Count) ($([math]::Round($elapsed.TotalSeconds,1))s)"
$withCats = ($results | Where-Object { $_.categories.Count -gt 0 }).Count
Write-Host "With categories: $withCats ($([math]::Round($withCats/$($results.Count)*100,1))%)"
$uncat = ($results | Where-Object { $_.categories.Count -eq 0 }).Count
Write-Host "Uncategorized: $uncat ($([math]::Round($uncat/$($results.Count)*100,1))%)"
$withMeta = ($results | Where-Object { $_.meta_categories.Count -gt 0 }).Count
Write-Host "With meta-categories: $withMeta"
$withPatents = ($results | Where-Object { $_.patent_numbers.Count -gt 0 }).Count
Write-Host "With patent numbers: $withPatents"
$withPerson = ($results | Where-Object { $_.primary_person -ne "" }).Count
Write-Host "With researcher name: $withPerson"
$withPreview = ($results | Where-Object { $_.content_preview.Length -gt 20 }).Count
Write-Host "With content preview: $withPreview"
$withUrl = ($results | Where-Object { $_.source_url -ne "" }).Count
Write-Host "With source URL: $withUrl"

Write-Host ""
Write-Host "=== CATEGORY COUNTS ==="
$results | ForEach-Object { $_.categories } | Where-Object { $_ } | Group-Object | Sort-Object Count -Descending | ForEach-Object { Write-Host "  $($_.Count)  $($_.Name)" }

Write-Host ""
Write-Host "=== META-CATEGORY COUNTS ==="
$results | ForEach-Object { $_.meta_categories } | Where-Object { $_ } | Group-Object | Sort-Object Count -Descending | ForEach-Object { Write-Host "  $($_.Count)  $($_.Name)" }

Write-Host ""
Write-Host "Done!"
