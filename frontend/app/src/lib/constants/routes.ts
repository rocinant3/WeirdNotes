
type RouteType = {
  title: string;
  href: string;
  isPublic: boolean
}

export const routes: RouteType[] = [
  {title: 'home', href: '/', isPublic: false},
  {title: 'lk', href: '/account', isPublic: false},
  {title: 'sign-in', href: '/auth/sign-in', isPublic: true},
  {title: 'sign-up', href: '/auth/sign-up', isPublic: true},
]
