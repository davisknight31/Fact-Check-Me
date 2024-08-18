import React from "react";

const HomePage: React.FC = () => {
  return (
    <main style={{ padding: "20px" }}>
      <h1>Welcome to the Home Page</h1>
      <p>This is the home page of our application.</p>
      <p>Here you can find the latest updates, news, and featured content.</p>
      <section>
        <h2>Featured Articles</h2>
        <ul>
          <li>How to get started with Next.js</li>
          <li>Building a responsive UI with React and Tailwind CSS</li>
          <li>Understanding Server-Side Rendering (SSR)</li>
        </ul>
      </section>
    </main>
  );
};

export default HomePage;
