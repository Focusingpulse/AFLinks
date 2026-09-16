// BioGeometry Dial Refactor — Phase 1A
// Implements Karim's BioGeometry Dial spec: two identical polarizer shapes oriented around a central axis
// Uses BQH ratios (1:1.6, 1:1.9, 1:2.8) and 16-count amplification

// ═══════════════════════════════════════════════════════════════════════════════
// BQH CONSTANTS [prescribed: Karim BQH ratios from rexresearch.com/biogeom/biogeom.htm]
// ═══════════════════════════════════════════════════════════════════════════════

const BG_CONSTANTS = {
    // BQH ratios [prescribed]
    PHI: 1.618,                    // Golden ratio — content:navigation split
    RATIO_1_6: 1.6,                // BQH ratio — primary proportions
    RATIO_1_9: 1.9,               // BQH ratio — secondary proportions
    RATIO_2_8: 2.8,               // BQH ratio — tertiary proportions
    
    // BG3 amplification count [prescribed: Karim's 16-identical-shapes rule]
    AMPLIFY_COUNT: 16,            // BG3 amplifies through 16 identical shapes
    
    // Dial dimensions using BQH ratios [prescribed]
    DIAL_OUTER_R: 212,            // Base outer radius
    DIAL_INNER_R: 212 / 1.618,    // ≈131 — golden ratio [prescribed]
    DIAL_POLARIZER_R: 186,        // Polarizer arc radius
    
    // Polarizer shape dimensions [prescribed]
    POLARIZER_SWEEP: 60,          // Arc sweep angle in degrees
    POLARIZER_WIDTH: 8,           // Arc stroke width
    
    // Negative-green caution [prescribed: Karim safety rule]
    // "Pyramids and domes emit negative green — harmful under continuous exposure"
    // Rule: No persistent pyramid/dome motifs in UI
    NEGATIVE_GREEN_CAUTION: 'no-persistent-pyramid-dome'
};

// ═══════════════════════════════════════════════════════════════════════════════
// POLARIZER SHAPE GENERATOR
// Two identical geometric polarizer shapes oriented around a central axis
// [prescribed: Karim BioGeometry Dial spec — Fig. 4 & Fig. 7 in patent]
// ═══════════════════════════════════════════════════════════════════════════════

function bgPolarizerPath(cx, cy, radius, startAngle, sweepAngle) {
    // Generate a curved polarizer arc path
    // [prescribed: Karim's polarizer shape — curved geometric form]
    const startRad = (startAngle - 90) * Math.PI / 180;
    const endRad = (startAngle + sweepAngle - 90) * Math.PI / 180;
    
    const x1 = cx + radius * Math.cos(startRad);
    const y1 = cy + radius * Math.sin(startRad);
    const x2 = cx + radius * Math.cos(endRad);
    const y2 = cy + radius * Math.sin(endRad);
    
    // Arc path
    const largeArc = sweepAngle > 180 ? 1 : 0;
    return `M ${x1.toFixed(2)} ${y1.toFixed(2)} A ${radius} ${radius} 0 ${largeArc} 1 ${x2.toFixed(2)} ${y2.toFixed(2)}`;
}

// ═══════════════════════════════════════════════════════════════════════════════
// BIOGEOMETRY DIAL RENDERER
// Replaces tick ring with two identical polarizer shapes
// [prescribed: BioGeometry Dial — two polarizers around central axis]
// ═══════════════════════════════════════════════════════════════════════════════

function kdRenderLock_BG(selIdx) {
    const svg = document.getElementById('kdLockSvg');
    const cx = 220, cy = 220;
    const N = kdLenses.length;
    const step = 360 / N;
    
    let h = '';
    
    // ════ DEFINITIONS ════
    h += `<defs>
        <!-- Face gradient [aesthetic] -->
        <radialGradient id="kdFace" cx="38%" cy="32%" r="75%">
            <stop offset="0%" stop-color="#3a5a5e"/>
            <stop offset="55%" stop-color="#1b3a40"/>
            <stop offset="100%" stop-color="#0c2530"/>
        </radialGradient>
        
        <!-- Polarizer gradient [prescribed: gold harmonic] -->
        <linearGradient id="kdPolarizer" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ffd166"/>
            <stop offset="50%" stop-color="#e8b64c"/>
            <stop offset="100%" stop-color="#c99a3a"/>
        </linearGradient>
        
        <!-- Knob gradient [aesthetic] -->
        <radialGradient id="kdKnob" cx="40%" cy="30%" r="70%">
            <stop offset="0%" stop-color="#f0c55f"/>
            <stop offset="55%" stop-color="#c99a3a"/>
            <stop offset="100%" stop-color="#8a6423"/>
        </radialGradient>
        
        <!-- Glow filter for active polarizer [aesthetic] -->
        <filter id="kdGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="4" result="blur"/>
            <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <!-- BG3 marker glow [prescribed: BG3 quality indicator] -->
        <filter id="kdStarGlow" x="-100%" y="-100%" width="300%" height="300%">
            <feGaussianBlur stdDeviation="3" result="blur"/>
            <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>`;
    
    // ════ OUTER FACE [aesthetic] ════
    // Using BQH ratio for inner circle [prescribed]
    const innerCircleR = Math.round(BG_CONSTANTS.DIAL_OUTER_R / BG_CONSTANTS.PHI);
    h += `<circle cx="${cx}" cy="${cy}" r="${BG_CONSTANTS.DIAL_OUTER_R}" fill="url(#kdFace)" stroke="rgba(232,182,76,0.45)" stroke-width="3"/>`;
    h += `<circle cx="${cx}" cy="${cy}" r="${innerCircleR}" fill="none" stroke="rgba(232,182,76,0.12)" stroke-width="1"/>`;
    
    // ════ POLARIZER PAIR [prescribed: BioGeometry Dial spec] ════
    // Two identical polarizer shapes oriented around central axis
    // Rotating group for drag interaction
    h += `<g id="kdPolarizers">`;
    
    // Calculate the angle for the selected lens to be at bottom (90°)
    const selAngle = 90;
    const rotation = selAngle - (selIdx * step);
    
    // Polarizer 1 — positioned at top [prescribed]
    const polarizer1Start = rotation - BG_CONSTANTS.POLARIZER_SWEEP / 2;
    h += `<path 
        d="${bgPolarizerPath(cx, cy, BG_CONSTANTS.DIAL_POLARIZER_R, polarizer1Start, BG_CONSTANTS.POLARIZER_SWEEP)}"
        fill="none" 
        stroke="url(#kdPolarizer)" 
        stroke-width="${BG_CONSTANTS.POLARIZER_WIDTH}"
        stroke-linecap="round"
        filter="url(#kdGlow)"
        data-bg-tier="prescribed"
        data-bg-source="Karim BioGeometry Dial — polarizer pair around central axis"
    />`;
    
    // Polarizer 2 — positioned 180° opposite [prescribed]
    const polarizer2Start = polarizer1Start + 180;
    h += `<path 
        d="${bgPolarizerPath(cx, cy, BG_CONSTANTS.DIAL_POLARIZER_R, polarizer2Start, BG_CONSTANTS.POLARIZER_SWEEP)}"
        fill="none" 
        stroke="url(#kdPolarizer)" 
        stroke-width="${BG_CONSTANTS.POLARIZER_WIDTH}"
        stroke-linecap="round"
        filter="url(#kdGlow)"
        data-bg-tier="prescribed"
        data-bg-source="Karim BioGeometry Dial — polarizer pair around central axis"
    />`;
    
    // ════ LENS POSITION MARKERS ════
    // Small dots marking each lens position [aesthetic]
    for (let i = 0; i < N; i++) {
        const angle = rotation + (i * step) - 90; // -90 to start from top
        const rad = angle * Math.PI / 180;
        const markerR = BG_CONSTANTS.DIAL_OUTER_R - 8;
        const x = cx + markerR * Math.cos(rad);
        const y = cy + markerR * Math.sin(rad);
        
        const isActive = i === selIdx;
        const focus = kdMode === 'paradigm' ? (kdLenses[i] || null) : kdFocusOf(kdLenses[i].name);
        const isFocus = focus && (kdMode === 'paradigm' ? (focus.af && focus.af > 0) : (focus.af_posts > 8));
        
        if (isActive) {
            // Active lens marker — larger and glowing [aesthetic]
            h += `<circle cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="6" fill="#ffd166" filter="url(#kdStarGlow)" data-bg-tier="aesthetic"/>`;
            
            // BG3 star marker for focus areas [prescribed: BG3 quality indicator]
            if (isFocus) {
                const starR = BG_CONSTANTS.DIAL_POLARIZER_R - 12;
                const sx = cx + starR * Math.cos(rad);
                const sy = cy + starR * Math.sin(rad);
                h += `<text x="${sx.toFixed(2)}" y="${(sy + 4).toFixed(2)}" font-size="14" text-anchor="middle" fill="#ffd166" filter="url(#kdStarGlow)" data-bg-tier="prescribed" data-bg-source="Karim BG3 quality marker">★</text>`;
            }
        } else {
            // Inactive lens marker [aesthetic]
            h += `<circle cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="${isFocus ? 4 : 3}" fill="${isFocus ? 'rgba(255,209,102,0.6)' : 'rgba(232,182,76,0.35)'}" data-bg-tier="aesthetic"/>`;
            
            // Smaller star for focus areas [prescribed]
            if (isFocus) {
                const starR = BG_CONSTANTS.DIAL_POLARIZER_R - 16;
                const sx = cx + starR * Math.cos(rad);
                const sy = cy + starR * Math.sin(rad);
                const smaller = N > 18 ? 8 : 10;
                h += `<text x="${sx.toFixed(2)}" y="${(sy + 3).toFixed(2)}" font-size="${smaller}" text-anchor="middle" fill="rgba(255,209,102,0.6)" data-bg-tier="prescribed" data-bg-source="Karim BG3 quality marker">★</text>`;
            }
        }
    }
    
    // ════ MINOR MARKS [prescribed: 16-count BG3 amplification] ════
    // 16 identical marks between each lens position
    const marksPerLens = BG_CONSTANTS.AMPLIFY_COUNT;
    const minorStep = step / marksPerLens;
    for (let i = 0; i < N * marksPerLens; i++) {
        const angle = rotation + (i * minorStep) - 90;
        const rad = angle * Math.PI / 180;
        const r1 = BG_CONSTANTS.DIAL_POLARIZER_R + 4;
        const r2 = BG_CONSTANTS.DIAL_OUTER_R - 4;
        const x1 = cx + r1 * Math.cos(rad);
        const y1 = cy + r1 * Math.sin(rad);
        const x2 = cx + r2 * Math.cos(rad);
        const y2 = cy + r2 * Math.sin(rad);
        
        h += `<line x1="${x1.toFixed(2)}" y1="${y1.toFixed(2)}" x2="${x2.toFixed(2)}" y2="${y2.toFixed(2)}" stroke="rgba(232,182,76,0.14)" stroke-width="1" data-bg-tier="prescribed" data-bg-source="Karim 16-count BG3 amplification"/>`;
    }
    
    h += `</g>`; // End polarizer group
    
    // ════ CENTER KNOB [aesthetic] ════
    // Keyhole design — kept for visual continuity [aesthetic]
    const knobR = Math.round(86 / BG_CONSTANTS.RATIO_1_6); // Using BQH ratio
    h += `<circle cx="${cx}" cy="${cy}" r="86" fill="url(#kdKnob)" stroke="rgba(58,44,16,0.9)" stroke-width="3"/>`;
    h += `<circle cx="${cx}" cy="${cy}" r="${knobR}" fill="none" stroke="rgba(58,44,16,0.55)" stroke-width="2"/>`;
    
    // Keyhole [aesthetic] — NOT a pyramid (negative-green caution respected)
    h += `<circle cx="${cx}" cy="${cy - 8}" r="14" fill="#231503"/>`;
    h += `<path d="M ${cx - 9} ${cy - 2} L ${cx + 9} ${cy - 2} L ${cx + 6} ${cy + 22} L ${cx - 6} ${cy + 22} Z" fill="#231503"/>`;
    h += `<circle cx="${cx}" cy="${cy - 8}" r="6" fill="#e8b64c"/>`;
    
    svg.innerHTML = h;
    
    // ════ UPDATE WINDOW LABEL ════
    const lens = kdLenses[selIdx];
    if (lens) {
        document.getElementById('kdWinLens').textContent = lens.name;
        if (kdMode === 'paradigm') {
            const p = lens;
            const pct = (p.pct != null) ? p.pct : (p.af && p.n ? Math.min(100, Math.round(p.af / p.n * 100)) : 0);
            const verdict = (p.span >= 15 && pct < 10)
                ? ` unexplored vein — archive holds only ${pct}% of what Aetherforce covers across ${p.span} fields`
                : (pct >= 40 ? ` — well-covered ground (${pct}% of AF output)` : ` spans ${p.span} fields`);
            document.getElementById('kdWinCount').textContent =
                `${p.n.toLocaleString()} docs · ★ ${p.af} AF posts · spans ${p.span} fields`;
            const winCount = document.getElementById('kdWinCount');
            let badge = document.getElementById('kdVerdict');
            if (!badge) {
                badge = document.createElement('div');
                badge.id = 'kdVerdict';
                badge.style.cssText = 'font-size:0.62rem;color:var(--gold-bright);letter-spacing:0.4px;text-transform:uppercase;margin-top:2px;';
                winCount.parentNode.insertBefore(badge, winCount.nextSibling);
            }
            badge.textContent = (p.span >= 15 && pct < 10 ? '⚡ ' : '') + verdict;
        } else {
            const f = kdFocusOf(lens.name);
            document.getElementById('kdWinCount').textContent = lens.n.toLocaleString() + ' docs' + (f && f.af_posts > 0 ? ` · ★ ${f.af_posts} Aetherforce posts` : '');
            const badge = document.getElementById('kdVerdict');
            if (badge) badge.textContent = '';
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// ROTATION HANDLER — Updated for polarizer group
// ═══════════════════════════════════════════════════════════════════════════════

function kdSetPolarizerRot(deg) {
    const g = document.getElementById('kdPolarizers');
    if (g) g.setAttribute('transform', `rotate(${Math.round(deg)} 220 220)`);
}

function kdResetPolarizerRot() {
    const g = document.getElementById('kdPolarizers');
    if (g) g.removeAttribute('transform');
}

// ═══════════════════════════════════════════════════════════════════════════════
// INTEGRATION NOTES
// ═══════════════════════════════════════════════════════════════════════════════
// 
// To integrate this refactor:
// 
// 1. Replace kdRenderLock() with kdRenderLock_BG()
// 2. Replace kdSetTickRot() with kdSetPolarizerRot()
// 3. Replace kdResetTickRot() with kdResetPolarizerRot()
// 4. Update kdSpinTo() to use polarizer rotation
// 5. Update drag handlers to reference 'kdPolarizers' group
//
// Three-tier labeling is implemented via data-bg-tier and data-bg-source attributes:
// - [prescribed] — implements specific Karim rule (cite source)
// - [aesthetic] — design choice, no prescriptive source
// - [tested] — has evidence (none yet)
//
// Negative-green caution is respected: no persistent pyramid/dome motifs.
// The keyhole shape is a rounded slot, not a pyramid.
