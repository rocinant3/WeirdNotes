<script lang="ts">
  import type {MenuItemType} from '$lib/types/sidebar'
  import {routes} from '$lib/constants/routes'


  const menuItems: MenuItemType[] = routes
  .filter((r) => r.isPublic === true)
  .map((r)  => ({href: r.href,  title: r.title}))

  let currentMenu = 'home';


</script>

<header class='bg-theme-light-primary w-full border-b-2 border-theme-light-secondary border-opacity-40 flex justify-between m-auto'>
  <div class="float-left w-16 pt-5" >
    <div class="leading-3 font-bold break-words text-theme-light-secondary">BRAIN</div>
    <div class="break-words font-bold text-theme-light-secondary">DUMP</div>
  </div>
  <div class="flex justify-center items-center py-6">
    {#each menuItems as menuItem}
      <a
        href={menuItem.href}
        class='px-5 text-center text-sm hover:bg-yellow-50 uppercase text-theme-light-secondary'
        on:click={() => currentMenu = menuItem.title}
      >
        {menuItem.title}
      </a>
    {/each}
  </div>
  <div class="float-right w-16 pt-6">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 float-right" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
    </svg>
  </div>
</header>

<style>
  header{
    max-height: 150px;
    width: 90vw;

  }
  </style>


