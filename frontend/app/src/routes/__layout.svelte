<script lang="ts">
  import Sidebar from '$lib/components/base/Sidebar.svelte'
  import MainContainer from '$lib/components/base/MainContainer.svelte'
  import "../styles/tailwind-output.css";

  let menuIsOpen = true;
  $: menuWidth = menuIsOpen ? 70 : 0;

  const toggleMenu = () => menuIsOpen = !menuIsOpen

</script>

<div class="flex">
  <Sidebar width={menuWidth} on:toggle={toggleMenu}/>
  <MainContainer offset={menuWidth}>
    <slot/>
  </MainContainer>
</div>

