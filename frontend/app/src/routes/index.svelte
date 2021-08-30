<svelte:head>
  <title>Главная</title>
</svelte:head>

<script>

  const posts = [
    "Lorem ipsum",
    "Lorem ipsum [2]",
    "Lorem ipsum [3]",
    "Lorem ipsum [4]",
  ]

</script>

<div class="flex flex-row mx-auto main-view-container m-8">
  <div class="flex flex-col h-full justify-between">
    <div class="text-sm font-thin">
      Today is
      <p class="text-sm font-normal">
        Monday
      </p>
    </div>

    <p class="break-words w-32 text-sm font-thin">Hello! My name is Igor. Its website is my way of sharing IT experience.</p>

  </div>
  <div class="w-full h-full ml-3 article-wrapper">
    <div class="main-article-card article-card pattern">
      Main Container
    </div>
    <div class="top-article-card article-card">
      Top container
    </div>
    <div class="bottom-article-card-1 article-card">
      Bottom 1 Container
    </div>
    <div class="bottom-article-card-2 article-card">
      Bottom 2 Container
    </div>

  </div>

</div>

  <style>
  .article-wrapper{
    display: grid;
    grid-template-columns: 2fr 1fr 1fr ;
    grid-auto-rows: minmax(100px, auto);
    grid-template-areas:
    "main top top"
    "main bottom-one bottom-two"
  }
  .main-article-card{
    grid-area: main;
  }
  .top-article-card{
    grid-area: top;
  }
  .bottom-article-card-1{
    grid-area: bottom-one;
  }
  .bottom-article-card-2{
    grid-area: bottom-two;
  }


  .main-view-container{
    width: 90vw;
  }
  </style>
