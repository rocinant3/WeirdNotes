<script lang="ts">
  import {createEventDispatcher} from 'svelte'

  import type {MenuItemType} from '$lib/types/sidebar'
  import authService from '$lib/services/auth'
  import {routes} from '$lib/constants/routes'


  const dispatch = createEventDispatcher();

  function toggleMenu() {
    dispatch('toggle');
  }

  const menuItems: MenuItemType[] = routes
  .filter((r) => r.isPublic === false)
  .map((r)  => ({href: r.href,  title: r.title}))

  let currentMenu = 'home';

  export let width = 0;

</script>

<span class="fixed top-0 left-0" on:click={toggleMenu}>toggle</span>


<div class='sidebar bg-yellow-200 h-screen' style={`width: ${width}px`}>
  <div class="mt-10">
    {#each menuItems as menuItem}
      <a
        href={menuItem.href}
        class:bg-yellow-100={currentMenu === menuItem.title}
        class='block w-full p-3 text-center hover:bg-yellow-100'
        on:click={() => currentMenu = menuItem.title}
      >
        {menuItem.title}
      </a>
    {/each}
  </div>
  <div class="pt-10">
    <button on:click={authService.logout}>logout</button>
  </div>
</div>


  <style>
  .sidebar{
    transition-property: width;
    transition-timing-function: ease-in;
    transition-duration: 200ms;
  }
  </style>
