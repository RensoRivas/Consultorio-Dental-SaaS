import './globals.css';
import { ReactNode } from 'react';

export const metadata = {
  title: 'Consultorio Dental SaaS',
  description: 'Gestión para clínicas dentales pequeñas'
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
