<script lang="ts">
  import type {UserStoreType} from '$lib/types/user'
  import userStore from '$lib/stores/user'


  const user: UserStoreType =  $userStore;
</script>


<div>
  <span>Email: {user.user.email}</span>
</div>
