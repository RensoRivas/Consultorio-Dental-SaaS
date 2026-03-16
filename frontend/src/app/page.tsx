import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="container">
      <h1>Consultorio Dental SaaS</h1>
      <p>MVP inicial en construcción.</p>
      <ul>
        <li>✅ Login de usuarios</li>
        <li>✅ Gestión de pacientes</li>
        <li>✅ Gestión de citas</li>
      </ul>
      <Link className="primary-btn" href="/patients">
        Ir a pacientes
      </Link>
    </main>
  );
}
