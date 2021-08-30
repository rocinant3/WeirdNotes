import * as cookie from 'cookie'

import { routes } from '$lib/constants/routes'


const validateToken = (token: string): boolean => {
  if (token && token !== ''){
    return true
  }
  return false
}


export async function handle({ request, resolve }) {
  const cookies = cookie.parse(request.headers.cookie || '');
  const isLoggedIn =  validateToken(cookies.token)

  request.locals.isLoggedIn = isLoggedIn;
  const response = await resolve(request);

  const publicPaths = routes.filter((r) => r.isPublic).map((r) => r.href)

  if (!isLoggedIn && !publicPaths.includes(request.path)) {
    return {
      status: 301,
      headers: {
        location: '/auth/sign-in'
      }
    };
  }
  return {
    ...response
  }
}

export function getSession(request) {
  const { isLoggedIn } = request.locals;
  return {
    isLoggedIn
  };
}
