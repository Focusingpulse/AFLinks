/* Peer-Lab renderer — reads labs.json and renders the four registries
   (protocols / equipment / variables / replication log) into the page.
   The "replication_verified" badge is awarded ONLY when a protocol has
   >=3 replication_log entries with verdict == "replicated" AND the number
   of distinct "hand" values among those entries is >=2 (the 3x2 rule). */

(function () {
  'use strict';

  function escapeHtml(str) {
    if (str === null || str === undefined) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  /* ── The 3x2 rule ────────────────────────────────────────────────
     Given a protocol and the full replication log, compute badge state:
       { verified: bool, replicated: int, hands: int } */
  function badgeState(protocol, log) {
    const repls = (log || []).filter(r =>
      r.protocol_id === protocol.id && r.verdict === 'replicated');
    const hands = new Set(repls.map(r => r.hand).filter(Boolean));
    const replicated = repls.length;
    const verified = replicated >= 3 && hands.size >= 2;
    return { verified, replicated, hands: hands.size };
  }

  function badgeHtml(state) {
    if (state.verified) {
      return '<span class="lb-badge verified" title="3+ independent replications by 2+ distinct hands">✅ replication_verified</span>';
    }
    return `<span class="lb-badge progress" title="Need 3 independent replications by 2+ distinct hands">🔬 in progress (${state.replicated}/3 replications, ${state.hands} hands)</span>`;
  }

  function registry(store, id, field) {
    const item = (store || []).find(x => x.id === id);
    return item ? item[field] || '' : '';
  }

  function renderProtocols(data) {
    const el = document.getElementById('labProtocols');
    if (!el) return;
    if (!data.protocols || !data.protocols.length) {
      el.innerHTML = '<div class="lb-empty">No protocols seeded yet.</div>';
      return;
    }
    const log = data.replication_log || [];
    el.innerHTML = '';
    data.protocols.forEach((p, i) => {
      const st = badgeState(p, log);
      const eqNames = (p.equipment || []).map(id => {
        const e = (data.equipment || []).find(x => x.id === id);
        return e ? escapeHtml(e.name) : escapeHtml(id);
      }).join(', ');
      const varNames = (p.variables || []).map(id => {
        const v = (data.variables || []).find(x => x.id === id);
        return v ? escapeHtml(v.name) : escapeHtml(id);
      }).join(', ');
      const card = document.createElement('div');
      card.className = 'lb-card';
      card.innerHTML = `
        <div class="lb-card-head" tabindex="0" role="button" aria-expanded="false"
             onclick="this.parentElement.classList.toggle('open')">
          <span class="lb-card-title">${escapeHtml(p.title)}</span>
          ${badgeHtml(st)}
          <span class="lb-chev">▸</span>
        </div>
        <div class="lb-card-body">
          <div class="lb-row"><span class="lb-k">Claim</span><span class="lb-v">${escapeHtml(p.claim)}</span></div>
          <div class="lb-row"><span class="lb-k">Objective</span><span class="lb-v">${escapeHtml(p.objective)}</span></div>
          <div class="lb-row"><span class="lb-k">Source</span><span class="lb-v">${(p.source_guides || []).map(escapeHtml).join(', ')}</span></div>
          <div class="lb-row"><span class="lb-k">Status</span><span class="lb-v">${escapeHtml(p.status)}</span></div>
          <div class="lb-row"><span class="lb-k">Equipment</span><span class="lb-v">${eqNames}</span></div>
          <div class="lb-row"><span class="lb-k">Variables</span><span class="lb-v">${varNames}</span></div>
          <div class="lb-row"><span class="lb-k">Expected outcome</span><span class="lb-v">${escapeHtml(p.expected_outcome)}</span></div>
          <div class="lb-row"><span class="lb-k">Safety</span><span class="lb-v">${escapeHtml(p.safety)}</span></div>
          ${p.steps && p.steps.length ? `<div class="lb-steps"><div class="lb-k">Protocol steps</div><ol>${p.steps.map(s => `<li>${escapeHtml(s)}</li>`).join('')}</ol></div>` : ''}
        </div>`;
      el.appendChild(card);
    });
  }

  function renderEquipment(data) {
    const el = document.getElementById('labEquipment');
    if (!el) return;
    const rows = (data.equipment || []).map(e => `
      <tr>
        <td>${escapeHtml(e.name)}</td>
        <td>${escapeHtml(e.category)}</td>
        <td>${escapeHtml(e.specs)}</td>
        <td class="lb-mon">${escapeHtml(e.cost_band)}</td>
        <td>${(e.source_options || []).map(escapeHtml).join(', ')}</td>
      </tr>`).join('');
    el.innerHTML = (data.equipment && data.equipment.length)
      ? `<table class="lb-table"><thead><tr><th>Item</th><th>Category</th><th>Specs</th><th>Cost</th><th>Source</th></tr></thead><tbody>${rows}</tbody></table>`
      : '<div class="lb-empty">No equipment seeded yet.</div>';
  }

  function renderVariables(data) {
    const el = document.getElementById('labVariables');
    if (!el) return;
    const rows = (data.variables || []).map(v => `
      <tr>
        <td>${escapeHtml(v.name)}</td>
        <td class="lb-mon">${escapeHtml(v.symbol)}</td>
        <td class="lb-mon">${escapeHtml(v.unit)}</td>
        <td>${escapeHtml(v.measurement_procedure)}</td>
        <td>${escapeHtml(v.typical_range)}</td>
      </tr>`).join('');
    el.innerHTML = (data.variables && data.variables.length)
      ? `<table class="lb-table"><thead><tr><th>Variable</th><th>Symbol</th><th>Unit</th><th>Measurement</th><th>Expected range</th></tr></thead><tbody>${rows}</tbody></table>`
      : '<div class="lb-empty">No variables seeded yet.</div>';
  }

  function verdictClass(v) {
    return { 'replicated': 'lb-ok', 'partial': 'lb-part', 'failed': 'lb-fail', 'inconclusive': 'lb-nil' }[v] || 'lb-nil';
  }

  function protocolTitle(data, id) {
    const p = (data.protocols || []).find(x => x.id === id);
    return p ? p.title : id;
  }

  function equipmentNames(data, ids) {
    return (ids || []).map(id => {
      const e = (data.equipment || []).find(x => x.id === id);
      return e ? escapeHtml(e.name) : escapeHtml(id);
    }).join(', ');
  }

  function renderLog(data) {
    const el = document.getElementById('labLog');
    if (!el) return;
    const rows = (data.replication_log || []).map(r => `
      <tr>
        <td>${escapeHtml(r.id)}</td>
        <td>${escapeHtml(protocolTitle(data, r.protocol_id))}</td>
        <td>${escapeHtml(r.hand)}</td>
        <td class="lb-mon">${escapeHtml(r.date)}</td>
        <td>${escapeHtml(r.setup)}</td>
        <td>${equipmentNames(data, r.equipment_used)}</td>
        <td><span class="lb-verdict ${verdictClass(r.verdict)}">${escapeHtml(r.verdict)}</span></td>
        <td class="lb-mon">${escapeHtml(r.data_file)}</td>
      </tr>`).join('');
    el.innerHTML = (data.replication_log && data.replication_log.length)
      ? `<table class="lb-table lb-log-table"><thead><tr><th>ID</th><th>Protocol</th><th>Hand</th><th>Date</th><th>Setup</th><th>Equipment</th><th>Verdict</th><th>Data file</th></tr></thead><tbody>${rows}</tbody></table>`
      : '<div class="lb-empty">No replication attempts logged yet — the yard is open for the first hands.</div>';
  }

  function renderSummary(data) {
    const el = document.getElementById('labSummary');
    if (!el) return;
    const log = data.replication_log || [];
    const elCount = (data.equipment || []).length;
    const varCount = (data.variables || []).length;
    const replCount = log.length;
    const verified = (data.protocols || []).filter(p => badgeState(p, log).verified).length;
    el.innerHTML = `
      <span class="lb-statik">${data.protocols.length} protocols</span>
      <span class="lb-statik">${elCount} equipment</span>
      <span class="lb-statik">${varCount} variables</span>
      <span class="lb-statik">${replCount} replication log entries</span>
      <span class="lb-statik">${verified} replication_verified</span>`;
  }

  function init() {
    const holder = document.getElementById('labRoot');
    if (!holder) return;
    fetch('labs.json')
      .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(data => {
        renderSummary(data);
        renderProtocols(data);
        renderEquipment(data);
        renderVariables(data);
        renderLog(data);
      })
      .catch(err => {
        holder.innerHTML = '<div class="lb-empty">Peer-Lab data not found yet (`labs/labs.json`). The registry is still seeding — check back soon.</div>';
      });
  }

  document.addEventListener('DOMContentLoaded', init);
})();
