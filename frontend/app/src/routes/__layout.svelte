<script lang="ts">
  import Header from '$lib/components/base/Header.svelte'
  import Footer from '$lib/components/base/Footer.svelte'
  import MainContainer from '$lib/components/base/MainContainer.svelte'
  import "../styles/tailwind-output.css";
</script>

<div class="flex flex-col layout-wrapper border-2 border-theme-light-secondary m-1">
  <Header/>
  <MainContainer>
    <slot/>
  </MainContainer>
  <Footer/>
</div>


  <style>
  .layout-wrapper{
    height: 99vh;
  }
  </style>

