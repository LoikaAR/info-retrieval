{/* res.json object fields example:
{"name": "360° Loop Gornergrat (Nr. 16)", "region": "Valais", "category": "Hiking trail", "distance": "0,5 km", "duration": "0,20 h", "ascent": "19 m"},
         */}

const ResultBox = () => {
  return (
    <div className="result-box">
      {/* <a className="result-link" href="https://www.geeksforgeeks.org/" target="_blank"  rel="noreferrer"><h2 className="result-title">
        Search Result (name)
      </h2></a> */}
      <a className="result-link" href="https://www.google.com/" target="_blank"  rel="noreferrer"><h2 className="result-title">
        Search Result (name)
      </h2></a>
      <div className="result-details">
        <h3 className="result-stats">
          Distance: aaa
          <br />
          Duration: aaa
          <br />
          Ascent: aaa
        </h3>
        <h3 className="result-category">
          Category: aaaaa
          <br />
          Region: aaa
        </h3>
      </div>
      <p className="result-description">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam nulla porttitor massa id. Nam libero justo laoreet sit amet cursus sit amet dictum. Mi sit amet mauris commodo quis imperdiet massa tincidunt nunc. Donec et odio pellentesque diam volutpat commodo sed egestas egestas. Lacus laoreet non curabitur gravida. Varius morbi enim nunc faucibus a.
      </p>
    </div>
  );
};

export default ResultBox;