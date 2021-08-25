<script context="module" lang="ts">



  export async function load({session}) {
    console.log('SESSION', session)
    if (session.isLoggedIn) {
      return {
        status: 301,
        redirect: '/'
      };
    }
    return {};
  }
</script>



<script lang="ts">
  import {session} from '$app/stores'

  import MainContainer from '$lib/components/base/MainContainer.svelte'
  import Snackbar from '$lib/components/base/Snackbar.svelte'
  import "../../styles/tailwind-output.css";

  console.log('SESSION 2', $session)
</script>

<Snackbar/>
<MainContainer>
  <slot/>
</MainContainer>
