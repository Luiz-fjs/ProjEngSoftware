'use client'

import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { useState } from "react";
import 'material-icons/iconfont/material-icons.css';

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [dark, setDark] = useState(false);

  return (
    <html lang="en" className={dark ? "dark" : ""}>
      <title>Terapp.IA</title>
      <body
        className={`dark:bg-black ${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <div className="fixed top-0 w-full flex flex-row h-10 m-2 z-3">
          <span className="rounded-full px-2 content-center dark:text-white dark:hover:bg-neutral-600 hover:bg-neutral-200 hover:cursor-pointer material-icons" onClick={() => {
            setDark(!dark);
          }}>dark_mode</span>
        </div>
        {children}
      </body>
    </html>
  );
}