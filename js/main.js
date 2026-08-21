// Weave-a-World · shared interactions

// ---------- Reveal-on-scroll ----------
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.05 }
);
document.querySelectorAll(".reveal").forEach((el) => revealObserver.observe(el));

// Anchor jumps (e.g. the Youth Action chips) can skip past elements faster
// than the observer fires, leaving them invisible. When navigating to a
// hash, instantly reveal the target and everything above it.
function revealThrough(target) {
  document.querySelectorAll(".reveal").forEach((el) => {
    if (el === target || el.compareDocumentPosition(target) & Node.DOCUMENT_POSITION_FOLLOWING) {
      el.classList.add("visible");
      revealObserver.unobserve(el);
    }
  });
}
function handleHash() {
  if (!location.hash) return;
  const target = document.getElementById(location.hash.slice(1));
  if (target) revealThrough(target.closest(".reveal") || target);
}
window.addEventListener("hashchange", handleHash);
handleHash();

// ---------- Collection screen: tab filtering ----------
const tabs = document.querySelectorAll(".tab");
const cards = document.querySelectorAll(".dye-card");
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => t.classList.remove("active"));
    tab.classList.add("active");
    const filter = tab.dataset.filter;
    cards.forEach((card) => {
      const match = filter === "all" || card.dataset.groups.split(" ").includes(filter);
      card.classList.toggle("hidden", !match);
    });
  });
});

// ---------- About page: count-up numbers ----------
const counters = document.querySelectorAll(".count[data-target]");
if (counters.length) {
  const countObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        countObserver.unobserve(el);
        const target = parseInt(el.dataset.target, 10);
        const duration = 1400;
        const start = performance.now();
        const tick = (now) => {
          const t = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - t, 3);
          el.textContent = Math.round(eased * target);
          if (t < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    },
    { threshold: 0.6 }
  );
  counters.forEach((el) => countObserver.observe(el));
}

// ---------- Splash: cloths weave with the cursor ----------
const splash = document.querySelector(".splash");
if (splash && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const layers = splash.querySelectorAll(".splash-layer");
  splash.addEventListener("mousemove", (e) => {
    const x = (e.clientX / window.innerWidth - 0.5) * 2;
    const y = (e.clientY / window.innerHeight - 0.5) * 2;
    layers.forEach((layer, i) => {
      const depth = (i + 1) * 10;
      layer.style.transform = `translate(${x * depth}px, ${y * depth}px)`;
    });
  });
}

// ---------- Poster page: table-of-contents scrollspy ----------
const tocLinks = document.querySelectorAll(".poster-toc a");
if (tocLinks.length) {
  const sections = Array.from(tocLinks).map((a) =>
    document.querySelector(a.getAttribute("href"))
  );
  const spy = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          tocLinks.forEach((a) => a.classList.remove("current"));
          const link = document.querySelector(
            `.poster-toc a[href="#${entry.target.id}"]`
          );
          if (link) link.classList.add("current");
        }
      });
    },
    { rootMargin: "-20% 0px -70% 0px" }
  );
  sections.forEach((s) => s && spy.observe(s));
}
