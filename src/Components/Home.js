import React from 'react';

function Home() {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Welcome to the Home Page!</h1>
        <p>This is a simple homepage for our React app.</p>
      </header>
      <main>
        <section className="home-content">
          <h2>Explore the App</h2>
          <p>Get started by navigating to different sections of the app!</p>
        </section>
      </main>
      <footer className="home-footer">
        <p>&copy; 2025 My React App</p>
      </footer>
    </div>
  );
}

export default Home;
