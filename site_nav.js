/*
 * site_nav.js — one navigation for every page of the Aetherforce Knowledge Vault.
 *
 * Why: the pages had drifted — different orders, different labels, different
 * emoji, missing entries. Chris (2026-09-15): "the main menu at the top needs
 * to stay consistent... those words should stay in the same order... even if
 * the palette is slightly changing on each page."
 *
 * Usage: include <script src="site_nav.js"></script> anywhere on a page.
 * It prepends a sticky nav bar to <body> and marks the current page "here".
 * Legacy in-page nav clusters should be removed when this is installed.
 * Per-page palettes stay free below the bar — the chrome is the constant.
 */
(function () {
  "use strict";

  // Canonical items — one order, one set of words, site-wide.
  var ITEMS = [
    { h: "index.html", t: "\uD83D\uDDDD Archive", d: "Browse every document — patents, papers & research" },
    { h: "vault.html", t: "\uD83D\uDD2D Vault", d: "The seams — where categories cross-reference each other" },
    { h: "library.html", t: "\u2693 Living Library", d: "Translations, researchers & the crew's finds" },
    { h: "translations.html", t: "\uD83C\uDF0D Translations", d: "The translation pipeline — works crossing languages" },
    { h: "lens.html", t: "\uD83D\uDCA0 Lens", d: "Cross-reference analysis — how authors think" },
    { h: "pathways.html", t: "\uD83D\uDDFA Pathways", d: "Curated five-document journeys into the hidden sciences" },
    { h: "synthesis.html", t: "\u2697 Fleet Briefings", d: "Reports — what the fleet is learning" },
    { h: "cosmology.html", t: "\uD83C\uDF0C Cosmology", d: "Twelve angles on the sky — standard & alternative" },
    { h: "masters.html", t: "\u2726 Masters", d: "The founding lineage" },
    { h: "insiders.html", t: "\u2726 Insiders", d: "Credentialed critics publishing in the mainstream journals" },
    { h: "qualitative-science.html", t: "\u25C8 Qualitative Science", d: "The physics of quality — and its lineage" },
    { h: "connectors.html", t: "\uD83D\uDD78 Connectors", d: "The people who connect the separate lines of research" },
    { h: "about.html", t: "\uD83E\uDDED About", d: "Who built this, and why" },
    { h: "methodology.html", t: "\uD83D\uDCDC Methodology", d: "How documents are sourced, curated & verified" },
    { h: "https://www.aetherforce.energy", t: "\uD83C\uDF10 Aetherforce", d: "The main site", ext: true }
  ];

  var CSS = [
    "#site-nav{position:sticky;top:0;z-index:1000;display:flex;gap:6px;align-items:center;",
    "overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none;",
    "background:rgba(11,15,20,.96);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);",
    "border-bottom:1px solid #6b5a2e;padding:8px 12px;box-sizing:border-box;}",
    "#site-nav::-webkit-scrollbar{display:none;}",
    "#site-nav .sn-a{flex:0 0 auto;font:500 13px/1.2 system-ui,-apple-system,sans-serif;",
    "color:#cbb98a;text-decoration:none;padding:7px 11px;border-radius:8px;",
    "border:1px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s,background .15s;}",
    "#site-nav .sn-a:hover{color:#e8b64c;border-color:#6b5a2e;background:rgba(232,182,76,.07);}",
    "#site-nav .sn-a.here{color:#e8b64c;border-color:#b98a2e;background:rgba(232,182,76,.1);",
    "box-shadow:0 0 10px rgba(232,182,76,.18);cursor:default;}",
    "#site-nav .sn-a.ext{margin-left:auto;border-color:#2a3440;}",
    "@media (max-width:640px){#site-nav{padding:6px 8px;}#site-nav .sn-a{font-size:12px;padding:6px 9px;}}"
  ].join("\n");

  function init() {
    if (document.getElementById("site-nav")) return;
    var here = (location.pathname.split("/").pop() || "index.html").toLowerCase();

    // Resolve relative item hrefs against this script's own URL so the nav
    // works from any depth (e.g. labs/labs.html).
    var base = "";
    try {
      var cs = document.currentScript;
      var src = cs && cs.src ? cs.src : "";
      base = src.slice(0, src.lastIndexOf("/") + 1);
    } catch (e) {}

    var style = document.createElement("style");
    style.textContent = CSS;
    document.head.appendChild(style);

    var nav = document.createElement("nav");
    nav.id = "site-nav";
    nav.setAttribute("aria-label", "Site navigation");
    ITEMS.forEach(function (it) {
      var a = document.createElement("a");
      a.className = "sn-a" + (it.ext ? " ext" : "");
      a.href = it.ext ? it.h : base + it.h;
      a.textContent = it.t;
      if (it.d) a.title = it.d;
      if (!it.ext && it.h.toLowerCase() === here) {
        a.className += " here";
        a.setAttribute("aria-current", "page");
      }
      if (it.ext) {
        a.target = "_blank";
        a.rel = "noopener";
      }
      nav.appendChild(a);
    });
    document.body.appendChild(nav); // prepend at the very top of the flow
    document.body.insertBefore(nav, document.body.firstChild);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
