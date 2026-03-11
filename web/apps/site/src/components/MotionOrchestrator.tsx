"use client";

import { useEffect } from "react";
import { usePathname } from "next/navigation";

const REVEAL_SELECTOR =
  ".topic-list-item, .topic-group-header, .concept-section, .search-result-card, .prev-next-link, .home-viz, .home-lab-card, .home-track-card, .home-dashboard, .home-insight-card, .visuals-card, .visuals-hero";

const PARALLAX_SELECTOR = "[data-parallax]";

function prefersReducedMotion() {
  if (typeof window === "undefined") return true;
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

export default function MotionOrchestrator() {
  const pathname = usePathname();

  useEffect(() => {
    if (prefersReducedMotion()) return;

    const root = document.documentElement;
    const revealTargets = Array.from(
      document.querySelectorAll<HTMLElement>(REVEAL_SELECTOR)
    );

    revealTargets.forEach((el) => el.classList.add("reveal"));

    const viewportHeight = window.innerHeight || 0;
    revealTargets.forEach((el) => {
      const rect = el.getBoundingClientRect();
      if (rect.top < viewportHeight * 0.9) {
        el.classList.add("is-visible");
      }
    });

    root.classList.add("has-scroll-anim");

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
          }
        }
      },
      { threshold: 0.15, rootMargin: "0px 0px -8% 0px" }
    );

    revealTargets.forEach((el) => observer.observe(el));

    const parallaxTargets = Array.from(
      document.querySelectorAll<HTMLElement>(PARALLAX_SELECTOR)
    );

    let raf = 0;
    const updateParallax = () => {
      raf = 0;
      const vh = window.innerHeight || 0;
      for (const el of parallaxTargets) {
        const max = parseFloat(el.dataset.parallax ?? "8");
        const rect = el.getBoundingClientRect();
        const offset = (rect.top + rect.height / 2 - vh / 2) / (vh / 2);
        const clamped = Math.max(-1, Math.min(1, offset));
        const translate = -clamped * max;
        el.style.setProperty("--parallax-y", `${translate.toFixed(2)}px`);
      }
    };

    const onScroll = () => {
      if (raf) return;
      raf = window.requestAnimationFrame(updateParallax);
    };

    if (parallaxTargets.length > 0) {
      updateParallax();
      window.addEventListener("scroll", onScroll, { passive: true });
      window.addEventListener("resize", onScroll);
    }

    return () => {
      observer.disconnect();
      if (raf) window.cancelAnimationFrame(raf);
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
    };
  }, [pathname]);

  return null;
}
