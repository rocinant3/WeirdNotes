<script lang="ts">

  export let offset: number = 0;
</script>


<div class="main-container h-screen flex justify-center items-center bg-gray-100" style={`width: calc(100% - ${offset}px)`}>
  <slot/>
</div>


  <style>
  .main-container{
    transition-property: width;
    transition-timing-function: ease-in;
    transition-duration: 200ms;
  }

  </style>


