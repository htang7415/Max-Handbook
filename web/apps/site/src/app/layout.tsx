import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import Sidebar from "@/components/Sidebar";
import MotionOrchestrator from "@/components/MotionOrchestrator";
import { buildNavItems, buildSidebarSections } from "@/lib/navigation";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";

export const metadata: Metadata = {
  title: "Max Handbook",
  description:
    "A handbook-style learning platform for fundamentals and demos.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const content = contentData as ContentIndex;
  const navItems = buildNavItems(content);
  const sections = buildSidebarSections(navItems);

  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <div className="site-header-inner">
            <div className="header-left">
              <Link href="/" className="header-logo">
                <span className="header-logo-icon">MH</span>
                <span>Max Handbook</span>
              </Link>
              <span className="header-tagline">
                Knowledge &middot; Visuals &middot; Code
              </span>
              <nav className="header-nav">
                <Link href="/visuals" className="header-nav-link">
                  Gallery
                </Link>
              </nav>
            </div>
            <form action="/search" className="header-search" role="search">
              <input
                type="search"
                name="q"
                placeholder="Search"
                className="header-search-input"
                aria-label="Search"
              />
              <button className="header-search-button" type="submit">
                <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                  <circle
                    cx="7"
                    cy="7"
                    r="4.5"
                    stroke="currentColor"
                    strokeWidth="1.4"
                  />
                  <path
                    d="M10.5 10.5L13 13"
                    stroke="currentColor"
                    strokeWidth="1.4"
                    strokeLinecap="round"
                  />
                </svg>
              </button>
            </form>
          </div>
        </header>
        <div className="handbook-shell">
          <Sidebar sections={sections} />
          <main className="handbook-main">{children}</main>
        </div>
        <MotionOrchestrator />
      </body>
    </html>
  );
}
