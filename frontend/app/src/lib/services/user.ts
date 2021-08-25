import Cookies from 'js-cookie'
import userStore, {initStoreState} from '$lib/stores/user'
import type {UserType, UserStoreType} from '$lib/types/user'


export function setUser(user: UserType){
  const storeData: UserStoreType = {
    user,
    isLoggedIn: true
  };
  Cookies.set('token', user.token)
  userStore.set(storeData);
}


export function removeUser(){
  Cookies.remove("token")
  userStore.set(initStoreState);
}


