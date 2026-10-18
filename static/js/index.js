const copyButton = document.getElementById('copy-citation');
const citation = document.getElementById('bibtex');
const status = document.getElementById('copy-status');
if (copyButton && citation && status) {
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(citation.textContent);
      status.textContent = 'Citation copied.';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(citation);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy.';
    }
  });
}

const gallery = document.getElementById('benchmark-gallery');
if (gallery) {
  const views = [...gallery.querySelectorAll('.benchmark-view')];
  const descriptions = [...document.querySelectorAll('[data-benchmark-view]')];
  const announcement = gallery.querySelector('.benchmark-status');
  let current = 0;
  let spinning = false;

  async function showView(index, moveFocus = false) {
    if (spinning || index === current) return;
    const outgoing = views[current].querySelector('.benchmark-image');
    const incoming = views[index].querySelector('.benchmark-image');
    const animate = !window.matchMedia('(prefers-reduced-motion: reduce)').matches
      && typeof outgoing.animate === 'function';
    spinning = true;
    if (animate) {
      await incoming.querySelector('img').decode().catch(() => {});
      await outgoing.animate([
        { transform: 'perspective(1400px) rotateY(0deg)' },
        { transform: 'perspective(1400px) rotateY(90deg)' }
      ], { duration: 280, easing: 'ease-in' }).finished.catch(() => {});
    }
    current = index;
    views.forEach((view, i) => { view.hidden = i !== index; });
    descriptions.forEach(description => {
      description.setAttribute('aria-pressed', String(Number(description.dataset.benchmarkView) === index));
    });
    if (moveFocus) incoming.focus({ preventScroll: true });
    if (animate) {
      await incoming.animate([
        { transform: 'perspective(1400px) rotateY(-90deg)' },
        { transform: 'perspective(1400px) rotateY(0deg)' }
      ], { duration: 280, easing: 'ease-out' }).finished.catch(() => {});
    }
    announcement.textContent = `${index === 0 ? 'Multiple-choice examples' : 'Nested chains'} shown.`;
    spinning = false;
  }

  descriptions.forEach(description => {
    description.setAttribute('role', 'button');
    description.tabIndex = 0;
    description.setAttribute('aria-pressed', String(Number(description.dataset.benchmarkView) === current));
    description.addEventListener('click', () => showView(Number(description.dataset.benchmarkView)));
    description.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        description.click();
      }
    });
  });
  views.forEach((view, index) => {
    const image = view.querySelector('.benchmark-image');
    image.setAttribute('role', 'button');
    image.setAttribute('aria-label', index === 0
      ? 'Show nested chains' : 'Show multiple-choice examples');
    image.addEventListener('click', (event) => {
      event.preventDefault();
      showView((current + 1) % views.length, true);
    });
    image.addEventListener('keydown', (event) => {
      if (event.key === ' ') {
        event.preventDefault();
        image.click();
      }
    });
  });
  views[1].hidden = true;
  gallery.querySelector('.benchmark-hint').hidden = false;
}

const carousel = document.querySelector('.instance-carousel');
if (carousel) {
  const slides = [...carousel.querySelectorAll('.instance-slide')];
  const selectors = [...carousel.querySelectorAll('[data-slide]')];
  const counter = carousel.querySelector('.instance-counter');
  let activeSlide = 0;
  function showSlide(index) {
    const previous = activeSlide;
    activeSlide = (index + slides.length) % slides.length;
    slides.forEach((slide, i) => { slide.hidden = i !== activeSlide; });
    selectors.forEach((button, i) => button.setAttribute('aria-pressed', String(i === activeSlide)));
    counter.textContent = `${activeSlide + 1} / ${slides.length} · ${selectors[activeSlide].textContent}`;
    if (previous !== activeSlide && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      slides[activeSlide].animate([
        { opacity: 0, transform: 'translateX(18px)' },
        { opacity: 1, transform: 'translateX(0)' }
      ], { duration: 220, easing: 'ease-out' });
    }
  }
  selectors.forEach(button => button.addEventListener('click', () => showSlide(Number(button.dataset.slide))));
  carousel.querySelectorAll('[data-direction]').forEach(button => {
    button.addEventListener('click', () => showSlide(activeSlide + Number(button.dataset.direction)));
  });
  carousel.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      showSlide(activeSlide + (event.key === 'ArrowRight' ? 1 : -1));
    }
  });
  let touchStart = null;
  const track = carousel.querySelector('.instance-slides');
  track.addEventListener('touchstart', event => {
    touchStart = event.touches.length === 1 ? [event.touches[0].clientX, event.touches[0].clientY] : null;
  }, { passive: true });
  track.addEventListener('touchend', event => {
    if (!touchStart) return;
    const dx = event.changedTouches[0].clientX - touchStart[0];
    const dy = event.changedTouches[0].clientY - touchStart[1];
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) showSlide(activeSlide + (dx < 0 ? 1 : -1));
    touchStart = null;
  }, { passive: true });
  track.addEventListener('touchcancel', () => { touchStart = null; });
  showSlide(0);
  carousel.querySelector('.instance-controls').hidden = false;
  counter.hidden = false;
}
