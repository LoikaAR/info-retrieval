
import { useState } from 'react';

const Dropdown = () => {
const activities = ['Hiking', 'Biking', 'Adventure'];

  const [isOpen, setIsOpen] = useState(false);
  const [selectedActivity, setSelectedActivity] = useState('');

  const handleDropdownClick = () => {
    setIsOpen(!isOpen);
  };

  const handleOptionClick = (activity) => {
    setSelectedActivity(activity);
    setIsOpen(false);
  };

  return (
      <div className="dropdown" onClick={handleDropdownClick}>
        <span className="selected-option">{selectedActivity || 'Select an activity'}</span>
        <ul className={`options ${isOpen ? 'active' : ''}`}>
          {activities.map((activity, index) => (
            <li key={index} onClick={() => handleOptionClick(activity)}>
              {activity}
            </li>
          ))}
        </ul>
      </div>
  );
};

export default Dropdown;



    // return (
    //     <>
    //         <div className="dropdown">
    //             <label htmlFor="activities">Choose Your Activity:</label>
    //             <div className="custom-select">
    //                 <span className="selected-option">Select an activity</span>
    //                 <ul id="activities" className="options">
    //                     {activities.map((activity, index) => (
    //                         <option key={index} value={activity.toLowerCase()}>{activity}</option>
    //                     ))}
    //                 </ul>
    //             </div>
    //         </div>
    //         <div className="dropdown">
    //             <label htmlFor="activities">Choose Your Activity:</label>
    //             <select name="activities" id="activities">
    //                 {activities.map((activity, index) => (
    //                     <option key={index} value={activity.toLowerCase()}>{activity}</option>
    //                 ))}
    //             </select>
    //         </div>
    //     </>


    // );
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
    //         <label for="activitys">Choose a activity:</label>
    //         <select name="activitys" id="activitys">
    //             <option value="volvo">Volvo</option>
    //             <option value="saab">Saab</option>
    //             <option value="opel">Opel</option>
    //             <option value="audi">Audi</option>
    //         </select>
    //         <input type="submit" value="Submit"></input>
    //         </form>
    //     </>
    // );

