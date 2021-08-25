import {writable} from './localStorageStore'
import type {UserType, UserStoreType} from '$lib/types/user'

const initialUser: UserType = {
  email: "",
  token: ""

}



export const initStoreState: UserStoreType = {
  user: initialUser,
  isLoggedIn: false
}



const store = writable('user', initStoreState);
export default store;
