const Dropdown = () => {
    const activities = ['Hiking', 'Biking', 'Adventure'];

return (
    <>
    <label htmlFor="activities">Choose an activity:</label>
    <select name="activities" id="cars">
      {activities.map((car, index) => (
        <option key={index} value={car.toLowerCase()}>{car}</option>
      ))}
    </select>
    </>
);
    // return (
    //     <>
    //         {/* <div className="dropdown">
    //             <button className="dropbtn">Dropdown</button>
    //             <div className="dropdown-content">
    //                 <a href="#">Link 1</a>
    //                 <a href="#">Link 2</a>
    //                 <a href="#">Link 3</a>
    //             </div>
    //         </div> */}
    //         <form action="">
    //         <label for="cars">Choose a car:</label>
    //         <select name="cars" id="cars">
    //             <option value="volvo">Volvo</option>
    //             <option value="saab">Saab</option>
    //             <option value="opel">Opel</option>
    //             <option value="audi">Audi</option>
    //         </select>
    //         <input type="submit" value="Submit"></input>
    //         </form>
    //     </>
    // );
};

export default Dropdown;