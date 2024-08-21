const API_URL = import.meta.env.VITE_API_URL

export async function classifyText (text: string) {
  const response = await fetch(`${API_URL}/classify`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text }),
  })
  return response.json()
}
