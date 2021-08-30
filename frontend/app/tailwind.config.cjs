module.exports = {
  mode: 'jit', // ⚠ Make sure to have this
  purge: ["./src/**/*.svelte"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        darcula: {
          background: '#2b2b2b',
          foreground: '#a9b7c6',
          "current-line": '#323232',
          selection: "#214283",
          green: "#379c1a"
        },
        theme: {
          light: {
            primary: "hsl(0, 0%, 90%)",
            secondary: "#3a3a3a",
          }
        }

      },

    },
  },
  variants: {
    extend: {animation: ['motion-safe']},
  },
  plugins: [],
}
