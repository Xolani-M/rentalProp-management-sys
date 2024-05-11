# rentalProp-management-sys
This project aims to create a system that streamlines the process of registering interest from prospective tenants and notifying the responsible agents.

## Development Process

1. **Understanding Requirements:**
   - Core objective: Manage tenants' interest in Bitprop's properties.
   - Key features: Property listing, registration, email notifications to agents.

2. **Researching Technologies:**
   - Frontend: HTML, CSS, JavaScript.
   - Backend: Python (Flask), SQLite for database.
   - External API for email notifications.

3. **Designing the System:**
   - User interface design with HTML/CSS, dynamic content with JavaScript.
   - Database schema for tenants, properties, agents.
   - Flask routes for user interactions and API calls.

4. **Setting Up Development Environment:**
   - Install Flask, SQLite, and necessary libraries.
   - Initialize Git repository for version control.

5. **Creating Backend Logic:**
   - Develop Python scripts for user interactions, database operations, and email notifications.
   - Define Flask routes for registering interest, agent login, and API endpoints.

6. **Building User Interface:**
   - Design HTML templates for frontend pages (property listings, registration, login).
   - Styling with CSS for a user-friendly interface.
   - Client-side validation and dynamic content loading with JavaScript.

7. **Database Setup and Management:**
   - Create SQLite database for storing tenant, property, and agent information.
   - Define database schemas, relationships, and constraints.

8. **Integrating External APIs:**
   - Research and integrate external API for email notifications to agents.
   - Implement API calls within Flask routes to trigger email notifications.

9. **Testing and Debugging:**
   - Thorough testing of frontend and backend components.
   - Debugging and resolving any issues encountered.



## Progress Update

## HTML Structure

### Header and Navigation
- Logo with a link to the homepage
- Search container with input field and search button using Font Awesome icons.

### Main Content
- Hero section with a title and description.
- Property list section for displaying available properties (to be dynamically rendered).
  
### Registration Modal
- Modal for registering interest in properties.
  - Name input field
  - Email input field
  - Phone number input field with validation
  - Submit button


## CSS Styles

### Global Styles
- Imported Google Font 'Poppins' for consistent typography across the site.
- Set basic styles for the body to reset margins and paddings.

### Header and Navigation Styles
- Styled the header with a background color, padding, and white text color.
- Aligned navigation items using flexbox with space-between and center alignment.
- Styled the logo with a bold font, white color, and removed underline from links.

### Search Container
- Designed the search container using flexbox for input and search button alignment.
- Styled input field and search button with appropriate padding, border, and background.

### Hero Section
- Set background image from Unsplash API with cover size and centered position.
- Added a semi-transparent overlay for better text visibility and visual appeal.
- Styled hero content with a max-width, padding, text color, and text shadow for readability.

### Property List Section
- Added padding to the property list section for spacing.
- Implemented a grid layout for displaying property cards with auto-fit columns.
- Styled property cards with background color, border, padding, border-radius, and box shadow.

### Registration Modal
- Designed the registration modal with a fixed position, semi-transparent background, and centered content.
- Styled modal content with padding, border, border-radius, box shadow, and close button.

### Form Styles
- Styled form inputs and buttons with margin, padding, border, border-radius, and background color.

### Responsive Design
- Included media queries for responsive design at different screen sizes (768px and 480px).
- Adjusted font sizes, modal width, header alignment, and grid columns for optimal viewing.
