import tailwindcss from "@headlessui/tailwindcss";
import forms from "@tailwindcss/forms";
import typography from "@tailwindcss/typography";
import type { Config } from "tailwindcss";
import animate from "tailwindcss-animate";

export default {
  content: ["./src/**/*.{html,js,jsx,md,mdx,svelte,ts,tsx,vue,svg}"],
  theme: {
    screens: {
      // These are the default media queries.
      // We're declaring them to make it easier to import and use in react for js checks
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      "2xl": "1536px",
    },
    extend: {
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
      boxShadow: {
        soft: "0px 0px 7px -5px rgba(0,0,0,0.75)",
        strong: "0px 0px 8px -5px rgba(0,0,0,1)",
      },
      colors: {
        primary: {
          20: "#F7F9FE",
          50: "#F0F4FE",
          100: "#DDE7FD",
          200: "#C1D4FB",
          500: "#4873EB",
          DEFAULT: "#4873EB",
        },
        gray: {
          20: "#979AA0",
        },
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
        outfit: ["Outfit", "sans-serif"],
      },
    },
  },
  plugins: [typography, forms, tailwindcss, animate],
} satisfies Config;
