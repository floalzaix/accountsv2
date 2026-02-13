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
  let y: number | string = date.getFullYear();
  let m: number | string = date.getMonth() + 1;
  let d: number | string = date.getDate();
  if (m < 10) {
    m = `0${m}`;
  }
  if (d < 10) {
    d = `0${d}`;
  }
  return `${y}-${m}-${d}`;
}