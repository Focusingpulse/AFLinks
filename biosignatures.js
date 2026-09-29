/* ═══════════════════════════════════════════════════════════════════════════
   BIOSIGNATURE SVG LIBRARY [prescribed: Karim BioGeometry — biosignature shapes]
   Source: rexresearch.com/biogeom/biogeom.htm (in-archive) + Karim, "Back to a
   Future for Mankind" (ch. on biosignatures: linear arrangements of shapes
   that emit BG3-quality energy through resonance of form).

   Honesty labels (Master Directive A — three-tier system):
     data-bg-tier="prescribed" — shape drawn from documented BioGeometry spec
     data-bg-tier="aesthetic"   — decorative choice, no BG source claimed
     data-bg-tier="tested"      — validated by our own replication (none yet)

   Usage:
     BGsig.render('wave', {w: 200, h: 24, class: 'divider'})
     BGsig.divider('wave')  → returns an SVG string for section dividers
   ═══════════════════════════════════════════════════════════════════════════ */

const BGsig = (() => {
    // [prescribed: BQH ratios from Karim's quality-of-emission measurements]
    const BQH = { PHI: 1.618, R16: 1.6, R19: 1.9, R28: 2.8 };

    /* Each biosignature returns raw SVG inner markup (no <svg> wrapper).
       viewBox space is 100 x 20 unless noted. Colors inherited via currentColor. */

    const shapes = {

        /* The Wave — undulating line, the foundational biosignature element
           [prescribed: Karim's wave shape; wavelength uses BQH 1:1.6 spacing] */
        wave: (o) => {
            const amp = o.h ? o.h * 0.3 : 6;
            const len = o.w || 100;
            const λ = len / BQH.R16; // [prescribed: 1:1.6]
            let d = `M 0 10`;
            for (let x = 0; x < len; x += λ) {
                d += ` q ${λ/4} ${-amp} ${λ/2} 0 q ${λ/4} ${amp} ${λ/2} 0`;
            }
            return `<path d="${d}" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" data-bg-tier="prescribed" data-bg-source="Karim wave biosignature, BQH 1:1.6 spacing"/>`;
        },

        /* Virtual Center — semi-circle with two radiating lines
           [prescribed: Karim's virtual center, used to balance a space and
            connect share/publish actions to the BG3 center. Fig. 9] */
        virtualCenter: (o) => {
            const r = o.r || 4;
            const cx = 50, cy = 16;
            return `<path d="M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}" fill="none" stroke="currentColor" stroke-width="1.5" data-bg-tier="prescribed" data-bg-source="Karim virtual center, semi-circle + two radiating lines"/>
                    <line x1="${cx}" y1="${cy}" x2="${cx}" y2="${(cy - r * BQH.R19).toFixed(2)}" stroke="currentColor" stroke-width="1.2" data-bg-tier="prescribed" data-bg-source="Karim virtual center, radiating line (1:1.9)"/>
                    <line x1="${cx}" y1="${cy}" x2="${(cx - r * BQH.R19).toFixed(2)}" y2="${cy}" stroke="currentColor" stroke-width="1.2" data-bg-tier="prescribed" data-bg-source="Karim virtual center, radiating line (1:1.9)"/>`;
        },

        /* 16-point star — BG3 amplification through 16 identical shapes
           [prescribed: Karim's 16-count amplification principle] */
        star16: (o) => {
            const cx = 50, cy = 10, r1 = o.r || 8, r2 = r1 / BQH.PHI;
            let pts = [];
            for (let i = 0; i < 32; i++) {
                const a = (i * 360 / 32 - 90) * Math.PI / 180;
                const r = i % 2 === 0 ? r1 : r2;
                pts.push(`${(cx + r * Math.cos(a)).toFixed(2)},${(cy + r * Math.sin(a)).toFixed(2)}`);
            }
            return `<polygon points="${pts.join(' ')}" fill="none" stroke="currentColor" stroke-width="1" data-bg-tier="prescribed" data-bg-source="Karim 16-count BG3 amplification star"/>`;
        },

        /* L-shape — the L-emitter, one of the most-cited biosignature elements
           [prescribed: Karim's L-shape; arm ratio 1:1.6] */
        lShape: (o) => {
            const a = o.a || 14, b = a / BQH.R16; // [prescribed: 1:1.6]
            return `<path d="M ${50 - a/2} 10 h ${a} v ${b} h ${-a} z" fill="none" stroke="currentColor" stroke-width="1.5" data-bg-tier="prescribed" data-bg-source="Karim L-shape biosignature, 1:1.6"/>`;
        }
    };

    function render(name, opts = {}) {
        const fn = shapes[name];
        if (!fn) return '';
        const w = opts.w || 100, h = opts.h || 20;
        const cls = opts.class ? ` class="${opts.class}"` : '';
        return `<svg viewBox="0 0 100 20" width="${w}" height="${h}"${cls} aria-hidden="true" style="color:${opts.color || 'inherit'}">${fn(opts)}</svg>`;
    }

    /* Section divider: wave + centered virtual center + wave (mirrored)
       [aesthetic arrangement of prescribed elements] */
    function divider(color) {
        return `<div class="bg-divider" data-bg-tier="aesthetic" data-bg-source="arrangement of prescribed Karim biosignatures" style="display:flex;align-items:center;justify-content:center;gap:14px;color:${color || 'var(--gold, #e8b64c)'};opacity:.55;margin:18px auto;max-width:420px">
            ${render('wave', { w: 120, h: 16 })}
            ${render('virtualCenter', { w: 40, h: 20 })}
            ${render('wave', { w: 120, h: 16, }) }
        </div>`;
    }

    return { shapes, render, divider, BQH };
})();

/* Auto-inject dividers at marked insertion points:
   any element with data-bgsig="divider" gets a biosignature divider. */
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-bgsig="divider"]').forEach(el => {
        el.innerHTML = BGsig.divider(el.dataset.bgColor);
    });
});
