type Patient = {
  id: number;
  first_name: string;
  last_name: string;
  email?: string | null;
  phone?: string | null;
};

async function fetchPatients(): Promise<Patient[]> {
  try {
    const response = await fetch('http://localhost:8000/patients', {
      cache: 'no-store'
    });

    if (!response.ok) {
      return [];
    }

    return response.json();
  } catch {
    return [];
  }
}

export default async function PatientsPage() {
  const patients = await fetchPatients();

  return (
    <main className="patients-wrapper">
      <section className="patients-card patients-modern-card">
        <header className="patients-header">
          <h1>Pacientes</h1>
          <button className="primary-btn" type="button">
            Agregar paciente
          </button>
        </header>

        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Email</th>
                <th>Teléfono</th>
              </tr>
            </thead>
            <tbody>
              {patients.length === 0 ? (
                <tr>
                  <td colSpan={4} className="empty-row">No hay pacientes registrados</td>
                </tr>
              ) : (
                patients.map((patient) => (
                  <tr key={patient.id}>
                    <td>{patient.id}</td>
                    <td>{patient.first_name} {patient.last_name}</td>
                    <td>{patient.email ?? '-'}</td>
                    <td>{patient.phone ?? '-'}</td>
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
