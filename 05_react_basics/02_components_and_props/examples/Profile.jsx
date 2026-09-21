export default function Profile({ name, skill }) {
  return (
    <article>
      <h2>{name}</h2>
      <p>Learning: {skill}</p>
    </article>
  );
}
