/**
   * A small wrapper because when clicked on the button to submit the 
   * blur is gone to quickly and the form is not submitted.
   * 
   * @param callback The close callback of the inplace component.
   * @param event The event that triggered the close.
   */
export function closeInplaceForm(
    callback: (event: any) => void,
    event: any
  ): void {
  setTimeout(() => {
    callback(event);
  }, 100);
}

/**
 * The purpose of this function is to get rid of the
 * time in the Date object of ts because it is not
 * accepted by the backend when expecting a date.
 * 
 * @param date The date to format.
 * @returns The formatted date to the format YYYY-MM-DD.
 */
export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}