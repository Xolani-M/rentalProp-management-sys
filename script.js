// Dummy data
const properties = [
    {
      id: 1,
      name: 'Sapphire Towers',
      location: 'Cape Town',
      rent: 9000,
      area: 1300,
      images: ['https://example.com/image1.jpg'],
      agentName: 'Alice Johnson',
      agentEmail: 'agent1@example.com'
    },
    {
      id: 2,
      name: 'Golden Crest Apartments',
      location: 'Cape Town',
      rent: 6000,
      area: 1000,
      images: ['https://example.com/image2.jpg'],
      agentName: 'Alice Johnson',
      agentEmail: 'agent1@example.com'
    },
    {
      id: 3,
      name: 'City View Suites',
      location: 'Stellenbosch',
      rent: 7500,
      area: 1100,
      images: ['https://example.com/image3.jpg'],
      agentName: 'Bob Williams',
      agentEmail: 'agent2@example.com'
    },
    {
      id: 4,
      name: 'Oceanfront Oasis',
      location: 'Hermanus',
      rent: 8500,
      area: 1200,
      images: ['https://example.com/image4.jpg'],
      agentName: 'Bob Williams',
      agentEmail: 'agent2@example.com'
    },
    {
      id: 5,
      name: 'Coastal View Residences',
      location: 'Camps Bay',
      rent: 5500,
      area: 950,
      images: ['https://example.com/image5.jpg'],
      agentName: 'Charlie Brown',
      agentEmail: 'agent3@example.com'
    },
    {
      id: 6,
      name: 'Riverside Apartments',
      location: 'Paarl',
      rent: 7000,
      area: 1050,
      images: ['https://example.com/image6.jpg'],
      agentName: 'Charlie Brown',
      agentEmail: 'agent3@example.com'
    },
    {
      id: 7,
      name: 'Parkside Residences',
      location: 'Somerset West',
      rent: 6000,
      area: 1000,
      images: ['https://example.com/image7.jpg'],
      agentName: 'David Smith',
      agentEmail: 'agent4@example.com'
    },
    {
      id: 8,
      name: 'Lakeview Apartments',
      location: 'Stellenbosch',
      rent: 5000,
      area: 900,
      images: ['https://example.com/image8.jpg'],
      agentName: 'David Smith',
      agentEmail: 'agent4@example.com'
    },
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
         <p>Rent: R ${property.rent}</p>
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


   // Show registration modalAdd
  function showRegistrationModal(propertyId) {
    modal.style.display = 'block';
    document.getElementById('property-id').value = propertyId;
  }
  
  // Close registration modal
  function closeModal() {
    modal.style.display = 'none';
    document.getElementById('interest-form').reset();
  }
  

  // Register interest form submission
  const interestForm = document.getElementById('interest-form');
  interestForm.addEventListener('submit', e => {
    e.preventDefault();
  
    const propertyId = document.getElementById('property-id').value;
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
  
    // Find the property object based on the selected property ID
    const selectedProperty = properties.find(property => property.id === parseInt(propertyId));
  
    // Get the agent email for the selected property
    const agentEmail = selectedProperty.agentEmail;
  
    // Send the form data and agent email to the backend API
    // Replace this with your actual API call
    console.log('Property ID:', propertyId);
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Phone:', phone)
    console.log('Agent Email:', agentEmail);
  
    closeModal();
  });


   // Close modal when clicking outside or pressing Esc key
   window.addEventListener('click', e => {
    if (e.target === modal) {
      closeModal();
    }
  });
  
  window.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      closeModal();
    }
  });
  
  // Close modal when clicking the close button
  closeBtn.addEventListener('click', closeModal);
  
  // Search and filter functionality
  function filterProperties() {
    const searchInput = document.getElementById('search-input');
    const searchTerm = searchInput.value.toLowerCase();
  
    const filteredProperties = properties.filter(property =>
      property.name.toLowerCase().includes(searchTerm) ||
      property.location.toLowerCase().includes(searchTerm)
    );
  
    renderProperties(filteredProperties);
  }
  
// Event listeners
document.getElementById('search-btn').addEventListener('click', filterProperties);
document.getElementById('search-input').addEventListener('input', filterProperties);

// Initial render
renderProperties();