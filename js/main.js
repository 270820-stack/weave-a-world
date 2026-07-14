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
