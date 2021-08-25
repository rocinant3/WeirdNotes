<script lang="ts">


  import authService from '$lib/services/auth'

  let email = "";
  let password = "";

  const onSubmit = () => {
    const ok = authService.signIn(email, password);

  }

</script>


<div class="bg-white shadow-md flex flex-col justify-center items-center p-5 rounded-md">
  <span class="text-gray-600 mb-3">Вход</span>
  <div class="my-4">
    <input class="form-input mb-2" bind:value={email} type="text" placeholder="Почта:"/>
    <input class="form-input" bind:value={password} placeholder="Пароль:"/>
  </div>
  <button class="button mt-3" on:click={onSubmit} type="button">Войти</button>
  <a href="/auth/sign-up" class="mt-5 text-center text-gray-600 text-sm block hover:underline"> Регистрация </a>
</div>
