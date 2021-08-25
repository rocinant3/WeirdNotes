type RequestMethod = "post"|"get";

export async function request(method: RequestMethod, url: string, data: any){
  const requestOptions = {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  };
  const response = await fetch(url, requestOptions);
  const json = await response.json()
  if (!response.ok){
    return Promise.reject(json)
  }
  return json
}

