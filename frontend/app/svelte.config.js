import preprocess from 'svelte-preprocess';
import { resolve } from 'path';
import adapter from '@sveltejs/adapter-node';
/** @type {import('@sveltejs/kit').Config} */


const config = {
  preprocess: [
    preprocess({
      defaults: {
        style: 'postcss'
      },
      postcss: true
    })
  ],

  kit: {
    adapter: adapter({
      out: 'build'
    }),
    hostHeader: 'X-Forwarded-Host',
    floc: true,
    target: '#svelte',

    vite: {
      ssr: {
        noExternal: []
      },
      resolve: {
        alias: {
          $stores: resolve('./src/stores'),
        }
      }
    }
  }
};

export default config;
