// Define the MotelCustomer class
class MotelCustomer {
    constructor(name, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
      this.name = name;
      this.birthDate = new Date(birthDate);
      this.gender = gender;
      this.roomPreferences = roomPreferences;
      this.paymentMethod = paymentMethod;
      this.mailingAddress = mailingAddress;
      this.phoneNumber = phoneNumber;
      this.stayDates = {
        checkIn: new Date(checkInDate),
        checkOut: new Date(checkOutDate)
      };
    }
  
    // Method to calculate age
    getAge() {
      const today = new Date();
      let age = today.getFullYear() - this.birthDate.getFullYear();
      const m = today.getMonth() - this.birthDate.getMonth();
      if (m < 0 || (m === 0 && today.getDate() < this.birthDate.getDate())) {
        age--;
      }
      return age;
    }
  
    // Method to calculate duration of stay
    getDurationOfStay() {
      const duration = Math.ceil((this.stayDates.checkOut - this.stayDates.checkIn) / (1000 * 60 * 60 * 24));
      return duration;
    }
  
    // Method to get a description of the customer
    getDescription() {
      return `
        <div>
          <h2>Customer Information</h2>
          <p>Name: ${this.name}</p>
          <p>Age: ${this.getAge()}</p>
          <p>Gender: ${this.gender}</p>
          <p>Room Preferences: ${this.roomPreferences.join(', ')}</p>
          <p>Payment Method: ${this.paymentMethod}</p>
          <p>Mailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state}, ${this.mailingAddress.zip}</p>
          <p>Phone Number: ${this.phoneNumber}</p>
          <p>Check-In Date: ${this.stayDates.checkIn.toDateString()}</p>
          <p>Check-Out Date: ${this.stayDates.checkOut.toDateString()}</p>
          <p>Duration of Stay: ${this.getDurationOfStay()} days</p>
        </div>
      `;
    }
  }
  
  // Export the MotelCustomer class
  export default MotelCustomer;
  