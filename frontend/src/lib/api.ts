export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

type PatientPayload = {
  first_name: string;
  last_name: string;
  dni: string;
  phone?: string;
  email?: string;
};

export type Patient = {
  id: number;
  first_name: string;
  last_name: string;
  dni: string;
  phone?: string | null;
  email?: string | null;
  created_at: string;
};

export async function getPatients(): Promise<Patient[]> {
  const response = await fetch(`${API_URL}/patients`, { cache: 'no-store' });
  if (!response.ok) {
    throw new Error('No se pudo cargar la lista de pacientes');
  }
  return response.json();
}

export async function createPatient(payload: PatientPayload): Promise<Patient> {
  const response = await fetch(`${API_URL}/patients`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Error inesperado' }));
    throw new Error(error.detail ?? 'No se pudo crear el paciente');
  }

  return response.json();
}
