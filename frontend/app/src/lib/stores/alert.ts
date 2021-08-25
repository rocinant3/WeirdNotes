import {writable} from 'svelte/store'
import type {AlertType} from '$lib/types/alert'



const initialValue: AlertType = {
  level: 'default',
  message: ""
}
const alertStore = writable(initialValue)

export default alertStore
