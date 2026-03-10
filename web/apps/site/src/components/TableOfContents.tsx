"use client";

import { useEffect, useState } from "react";
import { usePathname } from "next/navigation";

export interface TocHeading {
  id: string;
  text: string;
  level: number; // 2 or 3
}

interface TableOfContentsProps {
  headings: TocHeading[];
}

export default function TableOfContents({ headings }: TableOfContentsProps) {
  const pathname = usePathname();
  const [activeId, setActiveId] = useState<string>("");
  const filteredHeadings =
    pathname?.startsWith("/track/dsa/") || pathname?.startsWith("/track/ml/")
      ? headings.filter((heading) => !/^Pitfalls$/i.test(heading.text))
      : headings;

  useEffect(() => {
    if (filteredHeadings.length === 0) return;

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        }
      },
      { rootMargin: "-80px 0px -60% 0px", threshold: 0.1 }
    );

    for (const heading of filteredHeadings) {
      const el = document.getElementById(heading.id);
      if (el) observer.observe(el);
    }

    return () => observer.disconnect();
  }, [filteredHeadings]);

  if (filteredHeadings.length === 0) return null;

  return (
    <aside className="toc-aside">
      <p className="toc-title">On This Page</p>
      <nav className="toc-nav">
        {filteredHeadings.map((heading) => (
          <a
            key={heading.id}
            href={`#${heading.id}`}
            className={`toc-link ${heading.level === 3 ? "toc-link-nested" : ""} ${
              activeId === heading.id ? "toc-link-active" : ""
            }`}
          >
            {heading.text}
          </a>
        ))}
      </nav>
    </aside>
  );
}
