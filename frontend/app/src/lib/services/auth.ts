import {API_ADDR} from '$lib/constants/api'
import {request} from './requests'
import {setUser, removeUser} from './user'
import alertService from './alert'


function signIn(email: string, password: string){
  const endpoint = `${API_ADDR}/account/sign-in/`
  request('post', endpoint, {email, password}).then((data) => {
    setUser(data);
    window.location.reload()
  }).catch((e) => {
    alertService.warning("Ошибка")

  })
}


function signUp(email: string, password: string){
  const endpoint = `${API_ADDR}/account/sign-up/`
  request('post', endpoint, {email, password}).then((data) => {
    setUser(data);
    window.location.reload()
  }).catch((e) => {
    alertService.warning("Ошибка")
  })
}


function logout(){
  removeUser()
  window.location.reload()
}


const authService = {
  signIn,
  signUp,
  logout
}

export default authService;
