//Dummpy data
const properties = [
    {
      id: 1,
      name: 'Luxury Apartment',
      location: 'Cape Town',
      rent: 8000,
      area: 1200,
      images: ['https://example.com/image1.jpg', 'https://example.com/image2.jpg'],
      agentName: 'John Smith',
      agentEmail: 'agent1@example.com'
    },
    {
      id: 2,
      name: 'The Loft Life',
      location: 'observatory',
      rent: 4500,
      area: 900,
      images: ['https://example.com/image3.jpg'],
      agentName: 'John Smith',
      agentEmail: 'agent2@example.com'
    },
    {
        id: 3,
        name: 'The Urban Retreat',
        location: 'Milnerton',
        rent: 7000,
        area: 1000,
        images: ['https://example.com/image3.jpg'],
        agentName: 'GI Joe',
        agentEmail: 'agent2@example.com'
      },
      {
        id: 4,
        name: 'The Elevated Abode',
        location: 'Khayelitsha',
        rent: 5000,
        area: 900,
        images: ['https://example.com/image3.jpg'],
        agentName: 'GI Joe',
        agentEmail: 'agent2@example.com'
      }
  ];



   // Get modal elements
   const modal = document.getElementById('registration-modal');
   const closeBtn = document.getElementsByClassName('close-btn')[0];
   
   // Render properties on the page
   function renderProperties() {
     const propertyList = document.getElementById('property-list');
     propertyList.innerHTML = '';
   
     properties.forEach(property => {
       const li = document.createElement('li');
       li.innerHTML = `
         <h3>${property.name}</h3>
         <p>Location: ${property.location}</p>
         <p>Rent: $${property.rent}</p>
         <p>Area: ${property.area} sq.ft.</p>
         <p>Agent: ${property.agentName}</p>
         ${property.images.map(img => `<img src="${img}" alt="${property.name}">`).join('')}
         <button class="register-btn">Register Interest</button>
       `;
       propertyList.appendChild(li);
   
       const registerBtn = li.querySelector('.register-btn');
       registerBtn.addEventListener('click', () => showRegistrationModal(property.id));
     });
   }
