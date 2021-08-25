
<script lang="ts">
  import authService from '$lib/services/auth'

  let email = "";
  let password = "";
  let repeatPassword = "";

  const onSubmit = () => {
    authService.signUp(email, password);
  }
</script>


<div class="bg-white shadow-md flex flex-col justify-center items-center p-5 rounded-md">
  <span class="text-gray-600 mb-3">Регистрация</span>
  <div class="my-4">
    <input class="form-input mb-2" bind:value={email}  type="text" placeholder="Почта:"/>
    <input class="form-input" bind:value={password} placeholder="Пароль:"/>
    <input class="form-input mt-1" bind:value={repeatPassword} placeholder="Пароль еще раз:"/>
  </div>
  <button class="button mt-3" on:click={onSubmit} type="button">Зарегистрироваться</button>
  <a href="/auth/sign-in" class="mt-5 text-center text-gray-600 text-sm block hover:underline"> Войти </a>

</div>
