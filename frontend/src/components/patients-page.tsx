'use client';

import { FormEvent, useEffect, useMemo, useState } from 'react';
import { createPatient, getPatients, Patient } from '@/lib/api';

type FormState = {
  first_name: string;
  last_name: string;
  dni: string;
  phone: string;
  email: string;
};

const initialForm: FormState = {
  first_name: '',
  last_name: '',
  dni: '',
  phone: '',
  email: ''
};

export default function PatientsPageClient() {
  const [patients, setPatients] = useState<Patient[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState<FormState>(initialForm);

  async function fetchPatients() {
    try {
      setLoading(true);
      setError('');
      const data = await getPatients();
      setPatients(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error al cargar pacientes');
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchPatients();
  }, []);

  const sortedPatients = useMemo(
    () => [...patients].sort((a, b) => a.last_name.localeCompare(b.last_name)),
    [patients]
  );

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    try {
      setSubmitting(true);
      setError('');
      await createPatient({
        first_name: form.first_name,
        last_name: form.last_name,
        dni: form.dni,
        phone: form.phone || undefined,
        email: form.email || undefined
      });

      setForm(initialForm);
      setShowForm(false);
      await fetchPatients();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'No se pudo guardar el paciente');
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main className="patients-wrapper">
      <section className="patients-card">
        <header className="patients-header">
          <div>
            <h1>Pacientes</h1>
            <p>Gestiona los pacientes del consultorio.</p>
          </div>
          <button className="primary-btn" onClick={() => setShowForm((prev) => !prev)} type="button">
            Agregar paciente
          </button>
        </header>

        {showForm && (
          <form className="patients-form" onSubmit={onSubmit}>
            <input
              required
              placeholder="Nombre"
              value={form.first_name}
              onChange={(e) => setForm({ ...form, first_name: e.target.value })}
            />
            <input
              required
              placeholder="Apellido"
              value={form.last_name}
              onChange={(e) => setForm({ ...form, last_name: e.target.value })}
            />
            <input
              required
              placeholder="DNI"
              value={form.dni}
              onChange={(e) => setForm({ ...form, dni: e.target.value })}
            />
            <input
              placeholder="Teléfono"
              value={form.phone}
              onChange={(e) => setForm({ ...form, phone: e.target.value })}
            />
            <input
              type="email"
              placeholder="Email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
            />
            <button className="primary-btn" disabled={submitting} type="submit">
              {submitting ? 'Guardando...' : 'Guardar paciente'}
            </button>
          </form>
        )}

        {error && <p className="error-message">{error}</p>}

        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Nombre</th>
                <th>DNI</th>
                <th>Teléfono</th>
                <th>Email</th>
                <th>Alta</th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                <tr>
                  <td colSpan={5}>Cargando pacientes...</td>
                </tr>
              ) : sortedPatients.length === 0 ? (
                <tr>
                  <td colSpan={5}>Aún no hay pacientes cargados.</td>
                </tr>
              ) : (
                sortedPatients.map((patient) => (
                  <tr key={patient.id}>
                    <td>{patient.first_name} {patient.last_name}</td>
                    <td>{patient.dni}</td>
                    <td>{patient.phone ?? '-'}</td>
                    <td>{patient.email ?? '-'}</td>
                    <td>{new Date(patient.created_at).toLocaleDateString('es-AR')}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </section>
    </main>
  );
}
