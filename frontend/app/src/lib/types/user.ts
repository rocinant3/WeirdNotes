
type UserType = {
  token: string,
  email: string
}

type UserStoreType = {
  user: UserType,
  isLoggedIn: boolean
}

export type {UserType, UserStoreType};

