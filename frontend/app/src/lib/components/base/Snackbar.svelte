<script lang="ts">
  import {fly} from 'svelte/transition'

  import type {AlertType, AlertLevelType} from '$lib/types/alert'
  import alertService from '$lib/services/alert'
  import alertStore from '$lib/stores/alert'

  let message: string = "";
  let messageType: AlertLevelType = "default";


  alertStore.subscribe((a: AlertType) => {
    message = a.message
    messageType = a.level
  })


  const setTimeoutToClear = () => {
    setTimeout(() => {
      alertService.clear()
    }, 2000)
  }

</script>

{#if messageType !== "default"}
  <div class="snackbar-wrapper">
    <div class={`snackbar snackbar--${messageType}`}
      out:fly="{{y: -50, duration: 400}}"
      in:fly="{{y: -10, duration: 400}}"
      on:introstart="{setTimeoutToClear}">
      {message}
    </div>
  </div>
{/if}


<style>
  .snackbar-wrapper{
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .snackbar {
    position: fixed;
    top: 40px;
    z-index: 1000;
    min-width: 250px; /* Set a default minimum width */
    background-color: rgba(51, 51, 51, 0.91); /* Black background color */
    color: #fff; /* White text color */
    text-align: center; /* Centered text */
    border-radius: 2px; /* Rounded borders */
    padding: 16px; /* Padding */
  }

  .snackbar--warning {
    border-left: 10px solid #e24f46;
    border-radius: 2px;
  }


  .snackbar--success {
    border-left: 10px solid #79bfa5;
    border-radius: 2px;

  }


</style>
